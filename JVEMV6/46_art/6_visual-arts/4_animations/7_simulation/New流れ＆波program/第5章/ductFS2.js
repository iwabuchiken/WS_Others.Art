/*----------------------------------------------
     ductFS2.js
     速度-圧力法（フラクショナル・ステップ法）
     障害物の位置はX,Yともに可変、スタガード格子
     粒子アニメーション
-----------------------------------------------*/
var canvas; //キャンバス要素
var gl;//WebGL描画用コンテキスト
var height_per_width;//キャンバスのサイズ比
//animation
var fps ; //フレームレート
var lastTime;
var elapseTime = 0.0;//全経過時間
var elapseTime0 = 0.0;
var elapseTime1 = 0.0;
var elapseTimeN = 0.0;//無次元時間
var elapseTimeN0 = 0.0;
var flagStart = false;
var flagFreeze = false;
var flagStep = false;
var flagReset = false;

//数値計算
var Prs = [];//圧力
var velX = [];//staggered格子点のx速度
var velY = [];//staggered格子点のy速度
var velXgx = [];//速度微分
var velXgy = [];//速度微分
var velYgx = [];//速度微分
var velYgy = [];//速度微分
var VelX = [];//格子点の速度（表示格子点は圧力と同じ格子点）
var VelY = [];//格子点の速度（表示格子点は圧力と同じ格子点）
var Omg = [];//渦度（x,y速度で計算）
var type = [];//格子点のタイプ
var scale = new Vector3(1.0, 1.0, 0.0);//スケール調整
var ideal = 0;//側面理想流体

var flagPressIso = true;
var flagPressCol = false;
var flagVorticityIso = true;
var flagVorticityCol = false;
var flagVelocity = false;
var flagGrid = false;
var nLine = 20;//流線,ポテンシャルの表示本数
var arrowScale = 0.05;
var arrowWidth = 1;
var intervalV = 2;//速度矢印表示間隔

var deltaT = 0.005;
var Re = 500.0;//レイノルズ数

var maxPrs = 1.5;
var minPrs = -1.5;
var maxOmg = 20.0;
var minOmg = -20.0;

//粒子アニメーション
var sizeParticle = 5;
var speedCoef = 1.0;//速度倍率
var intervalP = 0.05;

//解析領域矩形構造体
function Rect()
{
  this.scale = 1.8;//表示倍率
  this.nMeshX = 80;//x方向割数（固定）
  this.nMeshY = 40; //y方向分割数（固定）
  this.size = new Vector3(2, 1, 0);//矩形ダクト領域のサイズ（固定）
  this.left0 = new Vector3(-1, -1, 0);//その左下位置
  this.obs_nX0 = 15;//左端から障害物中心までの距離(格子間隔の整数倍）
  this.obs_nY0 = 20;//下端から障害物中心までの距離(格子間隔の整数倍）
  this.obs_nWX = 2;//障害物の厚さ(ｘ方向,格子間隔の整数倍)
  this.obs_nWY = 6;//障害物の幅(ｙ方向,格子間隔の整数倍)
}
var rect = new Rect();
var NX, NY, DX, DY;
var NX, NX2, NY1, NY2;//障害物左端、右端、下端、上端

function webMain() 
{
  //canvas要素を取得する
  canvas = document.getElementById('WebGL');
  // WebGL描画用のコンテキストを取得する
  gl = WebGLUtils.setupWebGL(canvas);
  if (!gl) 
  {
    alert('WebGLコンテキストの取得に失敗');
    return;
  }
  var VS_SOURCE = document.getElementById("vs").textContent;
  var FS_SOURCE = document.getElementById("fs").textContent;

  
  if(!initGlsl(gl, VS_SOURCE, FS_SOURCE))
  {
    alert("GLSLの初期化に失敗");
    return;
  }
  
  //canvasをクリアする色を設定する
  gl.clearColor(1, 1, 1, 1);
  
  form1.deltaT.value = deltaT;
  form1.Re.value = Re;
  form1.nMeshX.value = rect.nMeshX;
  form1.nMeshY.value = rect.nMeshY;
  form1.obs_nX0.value = rect.obs_nX0;
  form1.obs_nY0.value = rect.obs_nY0;
  form1.obs_nWX.value = rect.obs_nWX;
  form1.obs_nWY.value = rect.obs_nWY;
  form2.scale.value = rect.scale;
  form2.nLine.value = nLine;
  //form2.psi.checked = flagStream;
  form2.omegaIso.checked = flagVorticityIso;
  form2.omegaCol.checked = flagVorticityCol;
  form2.pressIso.checked = flagVorticityIso;
  form2.pressCol.checked = flagVorticityCol;
  form2.velocity.checked = flagVelocity;
  form2.maxPrs.value = maxPrs;
  form2.minPrs.value = minPrs;
  form2.maxOmg.value = maxOmg;
  form2.minOmg.value = minOmg;
  
  initData();

//  initParticle();//粒子アニメーションの初期化

  var timestep = 0;
  var animate = function()
  {
    //繰り返し呼び出す関数を登録
    requestAnimationFrame(animate, canvas); //webgl-utilsで定義
    //時間計測
    var currentTime = new Date().getTime();
    var frameTime = (currentTime - lastTime) / 1000.0;//時間刻み[sec]
    elapseTime1 += frameTime;
    fps ++;
    if(elapseTime1 >= 0.5)
    {
      form1.fps.value = 2*fps.toString(); //1秒間隔で表示
      timestep = 1 / (2*fps);
      form1.step.value = timestep.toString();
      fps = 0;
      elapseTime1 = 0.0;
    }
    lastTime = currentTime;　
    if(flagStart)
    { 
      elapseTime += frameTime;
      elapseTimeN += deltaT;//数値計算上の経過時間（無次元時間）
        
      calculate(); 

      gl.clear(gl.COLOR_BUFFER_BIT);
      if(form2.particle.checked) drawParticle(timestep);  
      display();
      
      elapseTime0 = elapseTime;//現在の経過時間を保存
      elapseTimeN0 = elapseTimeN;//現在の経過時間を保存
      
      form1.e_time.value = elapseTime.toString();
      form1.n_time.value = elapseTimeN.toString();
      
      if(flagStep) { flagStart = false; } 
    }      
  }
  animate();

}

function initData()
{
  deltaT = parseFloat(form1.deltaT.value);
  Re = parseFloat(form1.Re.value);
  rect.nMeshX = parseInt(form1.nMeshX.value)
  NX = rect.nMeshX + 2;
  rect.nMeshY = parseInt(form1.nMeshY.value)
  NY = rect.nMeshY + 2;
  
  rect.obs_nX0 = parseFloat(form1.obs_nX0.value);
  rect.obs_nY0 = parseFloat(form1.obs_nY0.value);
  rect.obs_nWX = parseFloat(form1.obs_nWX.value);
  rect.obs_nWY = parseFloat(form1.obs_nWY.value);
  DX = rect.size.x / rect.nMeshX;//格子間隔
  DY = rect.size.y / rect.nMeshY;
  nX1 = rect.obs_nX0 - rect.obs_nWX/2;//
  nX2 = nX1 + rect.obs_nWX;
  nY1 = rect.obs_nY0 - rect.obs_nWY / 2;
  nY2 = rect.obs_nY0 + rect.obs_nWY / 2;

  initParticle();//粒子アニメーションの初期化
 
  var i, j;
  
  for(i = 0; i <= NX; i++)
  {//配列の2次元化
    type[i] = [];
    //Psi[i] = [];  //流れ関数
    Prs[i] = [];  //圧力
    Omg[i] = [];  //渦度
    VelX[i] = []; //ｘ方向速度
    VelY[i] = []; //ｙ方向速度
    velX[i] = [];//表示用も同じ
    velY[i] = [];
    velXgx[i] = [];   //ｘ方向微分
    velXgy[i] = [];   //ｙ方向微分
    velYgx[i] = [];   //ｘ方向微分
    velYgy[i] = [];   //ｙ方向微分
  }  

  //格子点のタイプ
  for(j = 0; j <= NY; j++)
  {
	for(i = 0; i <= NX; i++)
    {
	  type[i][j] = "INSIDE";//内点
	  if(j == 1) type[i][j] = "BOTTOM";//下側壁面
	  if(j == NY-1) type[i][j] = "TOP";//上側壁面
	  if(i == 1) type[i][j] = "INLET";//流入端
	  if(i == NX-1) type[i][j] = "OUTLET";//流出端
	  
	  if(i == nX1 && j > nY1 && j < nY2) type[i][j] = "OBS_LEFT";//障害物左端
	  if(i == nX2 && j > nY1 && j < nY2) type[i][j] = "OBS_RIGHT";//障害物右端
	  if(i > nX1 && i < nX2 && j == nY2) type[i][j] = "OBS_TOP";//障害物上端
	  if(i > nX1 && i < nX2 && j == nY1) type[i][j] = "OBS_BOTTOM";//障害物上端
	  if(i > nX1 && i < nX2 && j > nY1 && j < nY2) type[i][j] = "OBSTACLE";//障害物内部
	  //コーナー
	  if(i == nX1 && j == nY1) type[i][j] = "OBS_LL";
	  if(i == nX1 && j == nY2) type[i][j] = "OBS_UL";
	  if(i == nX2 && j == nY1) type[i][j] = "OBS_LR";
	  if(i == nX2 && j == nY2) type[i][j] = "OBS_UR";
	}
  }

  if(form2.ideal.checked) ideal = 1; else ideal = 0;

  //step1(初期値)
  //入口/出口は流速1
  for(j = 0; j <= NY; j++)  
	for (i = 0; i <= NX; i++)
	{
	  //圧力
	  Prs[i][j] = 0.0;
	  //速度
	  if(type[i][j] == "BOTTOM" || type[i][j] == "TOP" )　velX[i][j] = ideal;
      else if(type[i][j] == "OBS_LEFT" || type[i][j] === "OBS_RIGHT" || type[i][j] == "OBS_TOP" ||
         type[i][j] == "OBS_BOTTOM" || type[i][j] == "OBS_LL"|| type[i][j] == "OBS_UL"|| type[i][j] == "OBS_LR"|| type[i][j] == "OBS_UR") velX[i][j] = 0.0;
	  else velX[i][j] = 1.0;//その他はすべて1で初期化
      
      velY[i][j] = 0.0;//すべての速度ｙ成分は0
	  velXgx[i][j] = 0.0;
	  velXgy[i][j] = 0.0;
	  velYgx[i][j] = 0.0;
	  velYgy[i][j] = 0.0;
	  VelX[i][j] = velX[i][j];
	  VelY[i][j] = velY[i][j];
	  Omg[i][j] = 0.0;//渦度
    }

  maxPrs0 = -1000.0; minPrs0 = 1000.0;
  maxOmg0 = -1000.0; minOmg0 = 1000.0;

  //発散しないための目安を知るため
  var courant, diffNum;
  if(DX < DY)
  {
    courant = 1.0 * deltaT / DX;	
	diffNum = (1.0 / Re) * deltaT / (DX * DX);//拡散数
  }
  else
  {
 	courant = 1.0 * deltaT / DY;	
	diffNum = (1.0 / Re) * deltaT / (DX * DY);//拡散数
  }
  form1.courant.value = courant;
  form1.diffNum.value = diffNum;

  gl.clear(gl.COLOR_BUFFER_BIT);
  display();
}

function display()
{
  if(!flagStart) gl.clear(gl.COLOR_BUFFER_BIT);
  //flagStream = form2.psi.checked;
  flagPressIso = form2.pressIso.checked;
  flagPressCol = form2.pressCol.checked;
  flagVorticityIso = form2.omegaIso.checked;
  flagVorticityCol = form2.omegaCol.checked;
  flagVelocity = form2.velocity.checked;
  flagGrid = form2.grid.checked;
      
  gl.viewport(0, 0, canvas.width, canvas.height);
  height_per_width = canvas.height / canvas.width;//縦横の比率を一定にするための係数
	
  //計算領域描画
  drawRegion();

　//流線、等渦度線、圧力表示
  maxOmg = parseFloat(form2.maxOmg.value);
  minOmg = parseFloat(form2.minOmg.value);
  maxPrs = parseFloat(form2.maxPrs.value);
  minPrs = parseFloat(form2.minPrs.value);
  if( flagVorticityCol) drawColormap(Omg, minOmg, maxOmg);
  if( flagPressCol) drawColormapP(Prs, minPrs, maxPrs);
  if( flagVorticityIso ) drawContour(Omg, minOmg, maxOmg, "blue");
  if( flagPressIso) drawContourP(Prs, minPrs, maxPrs, "black");
  if( flagVelocity ) drawVelocity();
  if( flagGrid ) drawGrid();

  //下端／上端の壁
  drawLine(rect.left0.x, rect.left0.y, rect.left0.x + scale.x * rect.size.x, rect.left0.y, 2, "black");
  drawLine(rect.left0.x, rect.left0.y + rect.size.y * scale.y, rect.left0.x + scale.x * rect.size.x, rect.left0.y + rect.size.y * scale.y, 2, "black");
  //障害物
  var x_obs = rect.left0.x + rect.obs_nX0 * DX * scale.x; 
  var y_obs = rect.left0.y + rect.obs_nY0 * DY * scale.y;//rect.size.y * scale.y / 2; 
  drawRectangle(x_obs, y_obs, rect.obs_nWX * DX * scale.x, rect.obs_nWY * DY * scale.y, true, "light_gray", 0);
  drawRectangle(x_obs, y_obs, rect.obs_nWX * DX * scale.x, rect.obs_nWY * DY * scale.y, false, "black", 0);

}

function drawRegion()
{
  var s1, s2;
  if(canvas.width >= canvas.height) 
  {
    s1 = height_per_width;
    s2 = 1.0;
  }
  else
  {
    s1 = 1.0;
    s2 = 1 / height_per_width;
  }

  scale.x = rect.scale * s1;
  scale.y = rect.scale * s2;
  var sx = scale.x * rect.size.x / 2;//ダクトの幅は2*sx
  var sy = scale.y * rect.size.y / 2;//ダクトの高さは2*sy
  //ダクト
  drawRectangle(0, 0, 2*sx, 2*sy, false, "black", 0);

  var sxp = scale.x * (rect.size.x+DX) / 2;//ダクトの幅は2*sx
  var syp = scale.y * (rect.size.y+DY) / 2;//ダクトの高さは2*sy
  //圧力境界
  drawRectangle(0, 0, 2*sxp, 2*syp, false, "gray", 0);
  
  //ダクトの左下基準点
  rect.left0.x = - sx;
  rect.left0.y = - sy;
}

function calculate()
{
  var i, j;
  var iteration = 10;//最大繰り返し回数(Poisson方程式）
  var tolerance = 0.00001;//許容誤差
  var error = 0.0;
  var maxError = 0.0;
  var DX2 = DX * DX;
  var DY2 = DY * DY;
  var A1 = 0.5 * DY2 / (DX2 + DY2);
  var A2 = 0.5 * DX2 / (DX2 + DY2);
  var A3 = 0.25 * DX2*DY2 / (DX2 + DY2);
  var a, b, pp;

  //step2(速度の境界条件）
  //左右
  for (j = 0; j <= NY; j++) 
  {
    //流入口
    velX[0][j] =  velX[2][j];
    velX[1][j] =  1.0;
    velY[0][j] = -velY[1][j];//v=0
    //流出口
    velX[NX][j] =   velX[NX-2][j];
    velX[NX-1][j] = 1.0;
    velY[NX-1][j] =-velY[NX-2][j];//v=0
  }
  //上下
  for (i = 0; i <= NX; i++) 
  {
    velX[i][0] = -velX[i][1] + 2*ideal;
    velY[i][0] =  velY[i][2];
    velY[i][1] =  0.0;

    velX[i][NY-1] = -velX[i][NY-2] + 2*ideal;
    velY[i][NY] =  velY[i][NY-2];
    velY[i][NY-1] = 0.0;
  }

  //障害物左右
  for(j = nY1; j <= nY2; j++)
  {
    //左端
    velX[nX1+1][j] =  velX[nX1-1][j];
    velX[nX1][j]   =  0.0;
    velY[nX1][j]   = -velY[nX1-1][j];
    //右端
    velX[nX2-1][j] =  velX[nX2+1][j];
    velX[nX2][j]   =  0.0;
    velY[nX2-1][j] = -velY[nX2][j];
  }
  //障害物上下
  for(i = nX1; i <= nX2; i++)
  {
    //上端
    velX[i][nY2] = - velX[i][nY2+1];
    velY[i][nY2-1] = velY[i][nY2+1];
    velY[i][nY2]   = 0.0;
    //下端
    velX[i][nY1+1] = - velX[i][nY1];
    velY[i][nY1+1] = velY[i][nY1-1];
    velY[i][nY1]   = 0.0;
  }

  //step3(CIPによる速度輸送方程式)
  var vel = [];
  for(i = 0; i <= NX; i++) vel[i] = [];
  //x方向速度定義点における速度y
  for(i = 1; i < NX; i++)
    for(j = 1; j < NY; j++) 
      vel[i][j] = (velY[i-1][j] + velY[i][j] + velY[i-1][j+1] + velY[i][j+1]) / 4.0;

  methodCIP(velX, velXgx, velXgy, velX, vel);
  //y成分
  //y方向速度定義点における速度x
  for(i = 1; i < NX; i++)
	for(j = 1; j < NY; j++)
	  vel[i][j] = (velX[i][j] + velX[i][j-1] + velX[i+1][j-1] + velX[i+1][j]) / 4.0;
	
  methodCIP(velY, velYgx, velYgy, vel, velY);

  //Poisson方程式の右辺
  var D = [];
  for(i = 0; i <= NX; i++) D[i] = [];
  for (j = 1; j < NY; j++)
    for (i = 1; i < NX; i++)
	{
      if(type[i][j] == "OBS_LEFT" || type[i][j] === "OBS_RIGHT" || type[i][j] == "OBS_TOP" || type[i][j] == "OBS_BOTTOM" ||
         type[i][j] == "OBSTACLE" || type[i][j] == "OBS_LL"|| type[i][j] == "OBS_UL"|| type[i][j] == "OBS_LR"|| type[i][j] == "OBS_UR") continue;
	  D[i][j] = A3 * ((velX[i+1][j] - velX[i][j]) / DX + (velY[i][j+1] - velY[i][j]) / DY) / deltaT;
	}

  //反復法
  var cnt = 0;
  while (cnt < iteration)
  {
    maxError = 0.0;
	//圧力境界値
	for (j = 1; j < NY; j++) 
    {//左右
	  Prs[0][j] = Prs[1][j];//左端
	  Prs[NX-1][j] = Prs[NX-2][j];//右端
	}
	for (i = 0; i <= NX; i++)
    {//上下
	  Prs[i][0] = Prs[i][1] - 2.0 * velY[i][0] / (DY * Re);//下端
	  Prs[i][NY-1] = Prs[i][NY-2] + 2.0 * velY[i][NY] / (DY * Re);//上端
	}	

	//障害物
	for(j = nY1; j < nY2; j++)
	{
	  Prs[nX1][j] = Prs[nX1-1][j];//左端
	  Prs[nX2-1][j] = Prs[nX2][j];//右端
	}
	for(i = nX1; i < nX2; i++)
	{
	  Prs[i][nY1] = Prs[i][nY1-1];//下端
	  Prs[i][nY2-1] = Prs[i][nY2];//上端
	}

	//角
	Prs[nX1][nY1] = Prs[nX1-1][nY1-1];//左下
	Prs[nX1][nY2-1] = Prs[nX1-1][nY2];//左上
	Prs[nX2-1][nY2-1] = Prs[nX2][nY2];//右上
	Prs[nX2-1][nY1] = Prs[nX2][nY1-1];//右下

	for (j = 1; j < NY-1; j++)
	  for (i = 1; i < NX-1; i++)
	  {
      if(type[i][j] == "OBS_LEFT" || type[i][j] === "OBS_RIGHT" || type[i][j] == "OBS_TOP" || type[i][j] == "OBS_BOTTOM" ||
         type[i][j] == "OBSTACLE" || type[i][j] == "OBS_LL"|| type[i][j] == "OBS_UL"|| type[i][j] == "OBS_LR"|| type[i][j] == "OBS_UR") continue;
		pp = A1 * (Prs[i+1][j] + Prs[i-1][j]) + A2 * (Prs[i][j+1] + Prs[i][j-1]) - D[i][j];
		error = Math.abs(pp -  Prs[i][j]);
		if (error > maxError) maxError = error;
		Prs[i][j] = pp;//更新 
	  }
	  if (maxError < tolerance) break;
	  cnt++;
  }
  console.log("cnt = " + cnt + " maxError = " + maxError);

  //step5(スタガード格子点の速度ベクトルの更新）
  for (j = 1; j < NY-1; j++)
	for(i = 2; i < NX-1; i++)
	{	        
	  //if(type[i][j] != "INSIDE") continue;
	  velX[i][j] += - deltaT * (Prs[i][j] - Prs[i-1][j]) / DX;
	}
  for (j = 2; j < NY-1; j++)
	for(i = 1; i < NX-1; i++)
	{
	  //if(type[i][j] != "INSIDE") continue;
	  velY[i][j] += - deltaT * (Prs[i][j] - Prs[i][j-1]) / DY;
	}

  //表示のための速度は圧力と同じ位置で
  for(j = 1; j <= NY-2; j++)
	for(i = 1; i <= NX-2; i++)
	{
      VelX[i][j] = (velX[i][j] + velX[i+1][j]) / 2.0;
	  VelY[i][j] = (velY[i][j] + velY[i][j+1]) / 2.0;
	}

  //渦度
  for(i = 1; i < NX; i++)
	for (j = 1; j < NY; j++) 
	{
	  Omg[i][j] = 0.5 * ((VelY[i+1][j] - VelY[i-1][j]) / DX - (VelX[i][j+1] - VelX[i][j-1]) / DY);
	}
	
  //圧力・渦度の最大値・最小値
  for(i = 1; i < NX; i++)
	for (j = 1; j < NY; j++)
	{
	  if(Prs[i][j] > maxPrs0) maxPrs0 = Prs[i][j];
	  if(Prs[i][j] < minPrs0) minPrs0 = Prs[i][j];
	  if(Omg[i][j] > maxOmg0) maxOmg0 = Omg[i][j];
	  if(Omg[i][j] < minOmg0) minOmg0 = Omg[i][j];
//if(i==15) printf("j=%d prs=%f \n", j, Prs[i][j]);
	}
console.log("maxPrs= " + maxPrs0 + " minPrs = " + minPrs0);
console.log("maxOmg= " + maxOmg0 + " minOmg = " + minOmg0);
}

function methodCIP(f, gx, gy, vx, vy)
{
  var newF = [];//関数
  var newGx = [];//x方向微分
  var newGy = [];//y方向微分
  
  var i, j, ip, jp;
  for(i = 0; i <= NX; i++)
  {//配列の2次元化
    newF[i] = [];
    newGx[i] = [];
    newGy[i] = [];
  }

  var c11, c12, c21, c02, c30, c20, c03, a, b, sx, sy, x, y, dx, dy, dx2, dy2, dx3, dy3; 

  var i, j, ip, jp;
  for(i = 1; i < NX; i++)
	for(j = 1; j < NY; j++)
	{
	  //if(type[i][j] != "INSIDE") continue;
      if(i >=nX1 && i < nX2 && j >= nY1 && j < nY2) continue;
//      if(type[i][j] == "OBS_LEFT" || type[i][j] === "OBS_RIGHT" || type[i][j] == "OBS_TOP" || type[i][j] == "OBS_BOTTOM" ||
//         type[i][j] == "OBSTACLE" || type[i][j] == "OBS_LL"|| type[i][j] == "OBS_UL"|| type[i][j] == "OBS_LR"|| type[i][j] == "OBS_UR") continue;

	  if(vx[i][j] >= 0.0) sx = 1.0; else sx = -1.0;
	  if(vy[i][j] >= 0.0) sy = 1.0; else sy = -1.0;

	  x = - vx[i][j] * deltaT;
	  y = - vy[i][j] * deltaT;
	  ip = i - sx;//上流点
	  jp = j - sy;
	  dx = sx * DX;
	  dy = sy * DY;
	  dx2 = dx * dx;
	  dy2 = dy * dy;
	  dx3 = dx2 * dx;
	  dy3 = dy2 * dy;

	  c30 = ((gx[ip][j] + gx[i][j]) * dx - 2.0 * (f[i][j] - f[ip][j])) / dx3;
	  c20 = (3.0 * (f[ip][j] - f[i][j]) + (gx[ip][j] + 2.0 * gx[i][j]) * dx) / dx2;
	  c03 = ((gy[i][jp] + gy[i][j]) * dy - 2.0 * (f[i][j] - f[i][jp])) / dy3;
	  c02 = (3.0 * (f[i][jp] - f[i][j]) + (gy[i][jp] + 2.0 * gy[i][j]) * dy) / dy2;
	  a = f[i][j] - f[i][jp] - f[ip][j] + f[ip][jp];
	  b = gy[ip][j] - gy[i][j];
	  c12 = (-a - b * dy) / (dx * dy2);
	  c21 = (-a - (gx[i][jp] - gx[i][j]) * dx) / (dx2*dy);
	  c11 = -b / dx + c21 * dx;
	
      newF[i][j] = f[i][j] + ((c30 * x + c21 * y + c20) * x + c11 * y + gx[i][j]) * x
                 + ((c03 * y + c12 * x + c02) * y + gy[i][j]) * y;

      newGx[i][j] = gx[i][j] + (3.0 * c30 * x + 2.0 * (c21 * y + c20)) * x + (c12 * y + c11) * y;
      newGy[i][j] = gy[i][j] + (3.0 * c03 * y + 2.0 * (c12 * x + c02)) * y + (c21 * x + c11) * x;
	
      //粘性項に中央差分
	  newF[i][j] += deltaT * ( (f[i-1][j] + f[i+1][j] - 2.0 * f[i][j]) / dx2 
	             + (f[i][j-1] + f[i][j+1] - 2.0 * f[i][j]) / dy2 ) / Re;
	}

  //更新
  for(j = 1; j < NY; j++)
    for(i = 1; i < NX; i++)
	{
//      if(type[i][j] == "OBS_LEFT" || type[i][j] === "OBS_RIGHT" || type[i][j] == "OBS_TOP" || type[i][j] == "OBS_BOTTOM" ||
//         type[i][j] == "OBSTACLE" || type[i][j] == "OBS_LL"|| type[i][j] == "OBS_UL"|| type[i][j] == "OBS_LR"|| type[i][j] == "OBS_UR") continue;
      if(i >=nX1 && i < nX2 && j >= nY1 && j < nY2) continue;
	  //if(type[i][j] != "INSIDE") continue;
	  f[i][j] = newF[i][j];
	  gx[i][j] = newGx[i][j];
	  gy[i][j] = newGy[i][j];
	}
}

function drawContour(PP, minP, maxP, col)
{
  nLine = parseFloat(form2.nLine.value);
  
  var dp0 = (maxP - minP) / nLine;//流線間隔
  var pp;
  var x1, y1, x2, y2;
  var p = [], x = [], y = [];
  var i, j, k, m;
  var data = [];
 	
  //三角形セルに分割
  for (k = 0; k < nLine; k++)
  {
    //pp = minP + (k + 1) * dp0;
    pp = minP + k * dp0;
    for(j = 1; j <= NY-2; j++)
	{//(スタガード格子ではi=1,j=1が壁面）
      for(i = 1; i <= NX-2; i++)
	  {//三角形セルに分割
	    p[0] = PP[i][j]; x[0] = i * DX;     y[0] = j * DY;
	    p[1] = PP[i][j+1]; x[1] = i * DX;     y[1] = (j+1) * DY;
	    p[2] = PP[i+1][j+1]; x[2] = (i+1) * DX; y[2] = (j+1) * DY;
	    p[3] = PP[i+1][j]; x[3] = (i+1) * DX; y[3] = j * DY;
	    p[4] = p[0]; x[4] = x[0]; y[4] = y[0];//0番目に同じ
		//中心
		p[5] = (p[0] + p[1] + p[2] + p[3]) / 4.0;
		x[5] = (x[0] + x[1] + x[2] + x[3]) / 4.0;
		y[5] = (y[0] + y[1] + y[2] + y[3]) / 4.0;

        for(m = 0; m < 4; m++)//各三角形について
        {
          x1 = -10.0; y1 = -10.0; 
					
		  if((p[m] <= pp && pp < p[m+1]) || (p[m] > pp && pp >= p[m+1]))
		  {
            x1 = x[m] + (x[m+1] - x[m]) * (pp - p[m]) / (p[m+1] - p[m]);
			y1 = y[m] + (y[m+1] - y[m]) * (pp - p[m]) / (p[m+1] - p[m]);
          }
		  if((p[m] <= pp && pp <= p[5]) || (p[m] >= pp && pp >= p[5]))
		  {
		    if(x1 < 0.0)//まだ交点なし
			{
			  x1 = x[m] + (x[5] - x[m]) * (pp - p[m]) / (p[5] - p[m]);
			  y1 = y[m] + (y[5] - y[m]) * (pp - p[m]) / (p[5] - p[m]);
			}
			else//x1は見つかった
            {
			  x2 = x[m] + (x[5] - x[m]) * (pp - p[m]) / (p[5] - p[m]);
			  y2 = y[m] + (y[5] - y[m]) * (pp - p[m]) / (p[5] - p[m]);
			  data.push(rect.left0.x + scale.x * (x1-DX));
			  data.push(rect.left0.y + scale.y * (y1-DY));
			  data.push(rect.left0.x + scale.x * (x2-DX));
			  data.push(rect.left0.y + scale.y * (y2-DY));
			}			
          }
		  if((p[m+1] <= pp && pp <= p[5]) || (p[m+1] >= pp && pp >= p[5]))
		  {
		    if(x1 < 0.0)//まだ交点なし
			{
			  x1 = x[m+1] + (x[5] - x[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			  y1 = y[m+1] + (y[5] - y[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			}
			else//x1は見つかった
			{
			  x2 = x[m+1] + (x[5] - x[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			  y2 = y[m+1] + (y[5] - y[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);			  
			  data.push(rect.left0.x + scale.x * (x1-DX));
			  data.push(rect.left0.y + scale.y * (y1-DY));
			  data.push(rect.left0.x + scale.x * (x2-DX));
			  data.push(rect.left0.y + scale.y * (y2-DY));
	        }
          }
        }//m
	  }//j
	}//i  
  }//k
  drawLines(data, col);
}

function drawContourP(PP, minP, maxP, col)
{
  nLine = parseFloat(form2.nLine.value);
  
  var dp0 = (maxP - minP) / nLine;//流線間隔
  var pp;
  var x1, y1, x2, y2;
  var p = [], x = [], y = [];
  var i, j, k, m;
  var data = [];
 	
  //三角形セルに分割
  for (k = 0; k < nLine; k++)
  {
    //pp = minP + (k + 1) * dp0;
    pp = minP + k * dp0;
    for(j = 0; j <= NY-2; j++)
	{//(スタガード格子ではi=1,j=1が壁面）
      for(i = 0; i <= NX-2; i++)
	  {//三角形セルに分割
	    p[0] = PP[i][j]; x[0] = i * DX;     y[0] = j * DY;
	    p[1] = PP[i][j+1]; x[1] = i * DX;     y[1] = (j+1) * DY;
	    p[2] = PP[i+1][j+1]; x[2] = (i+1) * DX; y[2] = (j+1) * DY;
	    p[3] = PP[i+1][j]; x[3] = (i+1) * DX; y[3] = j * DY;
	    p[4] = p[0]; x[4] = x[0]; y[4] = y[0];//0番目に同じ
		//中心
		p[5] = (p[0] + p[1] + p[2] + p[3]) / 4.0;
		x[5] = (x[0] + x[1] + x[2] + x[3]) / 4.0;
		y[5] = (y[0] + y[1] + y[2] + y[3]) / 4.0;

        for(m = 0; m < 4; m++)//各三角形について
        {
          x1 = -10.0; y1 = -10.0; 
					
		  if((p[m] <= pp && pp < p[m+1]) || (p[m] > pp && pp >= p[m+1]))
		  {
            x1 = x[m] + (x[m+1] - x[m]) * (pp - p[m]) / (p[m+1] - p[m]);
			y1 = y[m] + (y[m+1] - y[m]) * (pp - p[m]) / (p[m+1] - p[m]);
          }
		  if((p[m] <= pp && pp <= p[5]) || (p[m] >= pp && pp >= p[5]))
		  {
		    if(x1 < 0.0)//まだ交点なし
			{
			  x1 = x[m] + (x[5] - x[m]) * (pp - p[m]) / (p[5] - p[m]);
			  y1 = y[m] + (y[5] - y[m]) * (pp - p[m]) / (p[5] - p[m]);
			}
			else//x1は見つかった
            {
			  x2 = x[m] + (x[5] - x[m]) * (pp - p[m]) / (p[5] - p[m]);
			  y2 = y[m] + (y[5] - y[m]) * (pp - p[m]) / (p[5] - p[m]);
			  data.push(rect.left0.x + scale.x * (x1-DX/2));
			  data.push(rect.left0.y + scale.y * (y1-DY/2));
			  data.push(rect.left0.x + scale.x * (x2-DX/2));
			  data.push(rect.left0.y + scale.y * (y2-DY/2));
			}			
          }
		  if((p[m+1] <= pp && pp <= p[5]) || (p[m+1] >= pp && pp >= p[5]))
		  {
		    if(x1 < 0.0)//まだ交点なし
			{
			  x1 = x[m+1] + (x[5] - x[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			  y1 = y[m+1] + (y[5] - y[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			}
			else//x1は見つかった
			{
			  x2 = x[m+1] + (x[5] - x[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);
			  y2 = y[m+1] + (y[5] - y[m+1]) * (pp - p[m+1]) / (p[5] - p[m+1]);			  
			  data.push(rect.left0.x + scale.x * (x1-DX/2));
			  data.push(rect.left0.y + scale.y * (y1-DY/2));
			  data.push(rect.left0.x + scale.x * (x2-DX/2));
			  data.push(rect.left0.y + scale.y * (y2-DY/2));
	        }
          }
        }//m
	  }//j
	}//i  
  }//k
  drawLines(data, col);
}

function drawColormap(PP, minP, maxP, col)
{
  var range0 = maxP - minP;
  var x0, y0, x1, y1, x2, y2, x3, y3;
  var pp = [], rr = [], gg = [], bb = [];
  var i, j, k;
  var vertices = [];
  var colors = [];

  for (i = 1; i <= NX-2; i++)
  {
    for (j = 1; j <= NY-2; j++)
    {
	  x0 = rect.left0.x + scale.x * (i-1) * DX;     
      y0 = rect.left0.y + scale.y * (j-1) * DY;
	  x1 = rect.left0.x + scale.x * i * DX;
      y1 = rect.left0.y + scale.y * (j-1) * DY;
	  x2 = rect.left0.x + scale.x * i * DX; 
      y2 = rect.left0.y + scale.y * j * DY;
	  x3 = rect.left0.x + scale.x * (i-1) * DX;     
      y3 = rect.left0.y + scale.y * j * DY;

	  pp[0] = (PP[i][j] - minP) / range0; 
	  pp[1] = (PP[i+1][j] - minP) / range0;
	  pp[2] = (PP[i+1][j+1] - minP) / range0; 
	  pp[3] = (PP[i][j+1] - minP) / range0;

      for(k = 0; k < 4; k++)
      {
        if(pp[k] < 0.25)
        {
		  rr[k] = 0.0; gg[k] = 4.0 * pp[k]; bb[k] = 1.0;
		}
		else if(pp[k] < 0.5)
		{
		  rr[k] = 0.0; gg[k] = 1.0; bb[k] = 4.0 * (0.5 - pp[k]);
		}
		else if(pp[k] < 0.75)
		{
		  rr[k] = 4.0 * (pp[k] - 0.5); gg[k] = 1.0; bb[k] = 0.0;
		}
		else
		{
		  rr[k] = 1.0; gg[k] = (1.0 - pp[k]) * 4.0; bb[k] = 0.0;
		}
      }
      //四角形（三角形2個分のデータ）
      vertices.push(x0); vertices.push(y0);
      vertices.push(x1); vertices.push(y1);
      vertices.push(x2); vertices.push(y2);
      vertices.push(x0); vertices.push(y0);
      vertices.push(x2); vertices.push(y2);
      vertices.push(x3); vertices.push(y3);
      colors.push(rr[0]); colors.push(gg[0]); colors.push(bb[0]); 
      colors.push(rr[1]); colors.push(gg[1]); colors.push(bb[1]); 
      colors.push(rr[2]); colors.push(gg[2]); colors.push(bb[2]); 
      colors.push(rr[0]); colors.push(gg[0]); colors.push(bb[0]); 
      colors.push(rr[2]); colors.push(gg[2]); colors.push(bb[2]); 
      colors.push(rr[3]); colors.push(gg[3]); colors.push(bb[3]); 
    }
  } 
  drawRectangles(vertices, colors);//swgShape2D.jsに実装
}

function drawColormapP(PP, minP, maxP, col)
{
  var range0 = maxP - minP;
  var x0, y0, x1, y1, x2, y2, x3, y3;
  var pp = [], rr = [], gg = [], bb = [];
  var i, j, k;
  var vertices = [];
  var colors = [];

  for (i = 0; i <= NX-2; i++)
  {
    for (j = 0; j <= NY-2; j++)
    {
	  x0 = rect.left0.x + scale.x * (i * DX -DX/2);     
      y0 = rect.left0.y + scale.y * (j * DY -DY/2);
	  x1 = rect.left0.x + scale.x * ((i+1) * DX -DX/2);
      y1 = rect.left0.y + scale.y * (j * DY - DY/2);
	  x2 = rect.left0.x + scale.x * ((i+1) * DX - DX/2); 
      y2 = rect.left0.y + scale.y * ((j+1) * DY - DY/2);
	  x3 = rect.left0.x + scale.x * (i * DX - DX/2);     
      y3 = rect.left0.y + scale.y * ((j+1) * DY - DY/2);

	  pp[0] = (PP[i][j] - minP) / range0; 
	  pp[1] = (PP[i+1][j] - minP) / range0;
	  pp[2] = (PP[i+1][j+1] - minP) / range0; 
	  pp[3] = (PP[i][j+1] - minP) / range0;

      for(k = 0; k < 4; k++)
      {
        if(pp[k] < 0.25)
        {
		  rr[k] = 0.0; gg[k] = 4.0 * pp[k]; bb[k] = 1.0;
		}
		else if(pp[k] < 0.5)
		{
		  rr[k] = 0.0; gg[k] = 1.0; bb[k] = 4.0 * (0.5 - pp[k]);
		}
		else if(pp[k] < 0.75)
		{
		  rr[k] = 4.0 * (pp[k] - 0.5); gg[k] = 1.0; bb[k] = 0.0;
		}
		else
		{
		  rr[k] = 1.0; gg[k] = (1.0 - pp[k]) * 4.0; bb[k] = 0.0;
		}
      }
      //四角形（三角形2個分のデータ）
      vertices.push(x0); vertices.push(y0);
      vertices.push(x1); vertices.push(y1);
      vertices.push(x2); vertices.push(y2);
      vertices.push(x0); vertices.push(y0);
      vertices.push(x2); vertices.push(y2);
      vertices.push(x3); vertices.push(y3);
      colors.push(rr[0]); colors.push(gg[0]); colors.push(bb[0]); 
      colors.push(rr[1]); colors.push(gg[1]); colors.push(bb[1]); 
      colors.push(rr[2]); colors.push(gg[2]); colors.push(bb[2]); 
      colors.push(rr[0]); colors.push(gg[0]); colors.push(bb[0]); 
      colors.push(rr[2]); colors.push(gg[2]); colors.push(bb[2]); 
      colors.push(rr[3]); colors.push(gg[3]); colors.push(bb[3]); 
    }
  } 
  drawRectangles(vertices, colors);//swgShape2D.jsに実装
}

function drawVelocity()
{
  arrowScale = parseFloat(form2.arrowScale.value);;
  arrowWidth = parseFloat(form2.arrowWidth.value);
  intervalV = parseFloat(form2.intervalV.value);
  var i, j;

  //描画
  var theta, mag, x0, y0;
  for(i = 0; i < NX-1; i++)
  {
    if(i % intervalV != 0) continue;
    for (j = 0; j < NY-1; j++)
	{
	  if(j % intervalV != 0) continue;
	  if(type[i][j] == "OBSTACLE") continue;
	  if(type[i][j] == "OBS_LEFT") continue;	  
      if(type[i][j] == "OBS_RIGHT") continue;
	  if(type[i][j] == "OBS_TOP") continue;

	  mag = Math.sqrt(velX[i][j] * velX[i][j] + velY[i][j] * velY[i][j]);
	  if(mag > 10.0) continue;
	  theta = Math.atan2(velY[i][j], velX[i][j]);
	  x0 = rect.left0.x + scale.x * i * DX;
      y0 = rect.left0.y + scale.y * j * DY;
	  drawArrow(x0, y0, mag * arrowScale, arrowWidth, "black", theta);
	}
  }
}

function drawGrid()
{
  var i, j;
  for(i = 0; i < NX-1; i++)
  {
    drawLine(rect.left0.x + scale.x * i * DX, rect.left0.y,
      rect.left0.x + scale.x * i * DX, rect.left0.y + scale.y * rect.size.y, 1, "black");
  }
  for(j = 1; j < NY-1; j++)
  {
    drawLine(rect.left0.x, rect.left0.y + scale.y * j * DY,
     rect.left0.x + scale.x * rect.size.x, rect.left0.y + scale.y * j * DY, 1, "black");
  }
}

//-----------------------------------------------------------------
function Particle2D()
{
  this.pos = new Vector3();
  this.vel = new Vector3();
  this.col = "red";
}
var countP = 0;
var pa = [];//particle
var sizeP = 3;
var speedCoef = 0.1;
var countPeriod = 0;
var period = 0.1;//[s]
var numMaxP =10000;//最大個数
var num0 = 100;
var typeP = 2;

function initParticle()
{
  //粒子インスタンス
  for(var i = 0; i < numMaxP; i++) pa[i] = new Particle2D();
}

function drawParticle(dt)
{
//console.log(" dt = " + dt + " speedCoef = " + speedCoef);
  flagPoint = true;  
  var k, k0, K1, K2 = 0;
  var dataP = []; 
  var dataQ = [];
  var vel = new Vector3(); 
 
  if(!flagFreeze && countPeriod == 0)
  {
    for(k0 = 0; k0 < num0; k0++)
	{
	  k = countP + k0;
	  createParticle(k);
	}
	countP += num0;
  }

  K1 = 0;
  K2 = 0;
  for(k = 0; k < numMaxP; k++)
  {
    vel = getVelocityParticle(pa[k].pos);

	if(!flagFreeze) {
      pa[k].pos.x += vel.x * dt * speedCoef;
      pa[k].pos.y += vel.y * dt * speedCoef;
    }
	if(pa[k].pos.x >= 0.0 && pa[k].pos.x < rect.size.x 
			&& pa[k].pos.y >= 0.0 && pa[k].pos.y < rect.size.y) 
    { 
      if( pa[k].col == "red")
      {
        dataP[2*K1] = rect.left0.x + pa[k].pos.x * scale.x; 
        dataP[2*K1+1] = rect.left0.y + pa[k].pos.y * scale.y; 
        K1++;
      }
      else
      {
        dataQ[2*K2] = rect.left0.x + pa[k].pos.x * scale.x; 
        dataQ[2*K2+1] = rect.left0.y + pa[k].pos.y * scale.y; 
        K2++;
      }
      
    }
    else{
      if( countPeriod == 0) createParticle(k); 
    }
  }

  drawPoints(dataP, sizeP, typeP, "red");
  drawPoints(dataQ, sizeP, typeP, "blue");
  
  if(countP > numMaxP - num0) countP = 0;
  
  countPeriod += dt;
  if(countPeriod > period){
    countPeriod = 0;
  }
}
function createParticle(k)
{
console.log("k = " + k + " x = " + pa[k].pos.x);
  pa[k].pos.x = 0.01;//左端(left0)からの位置
  if(k % 2 == 0) {pa[k].pos.y = getRandom(0, rect.size.y / 2); pa[k].col = "red";}
  else {pa[k].pos.y = getRandom(rect.size.y / 2, rect.size.y);  pa[k].col = "blue";}
}

function getVelocityParticle(pos)
{
  var vel = new Vector3();

  var i, j, I, J;

  //格子番号を取得
  I = 0; J = 0;
  for(i = 0; i < NX; i++)
  {
	if(i * DX < pos.x && (i+1) * DX > pos.x) I = i;
  }
  for(j = 0; j < NY; j++)
  {
 	if(j * DY < pos.y && (j+1) * DY > pos.y) J = j;
  }
//if(J>=20 && J <= 25)console.log(" x = " + pos.x + " y = " + pos.y + " I = " + I + " J = " + J + " v.x = " + VelX[I][J] + " v.y = " + VelY[I][J]);
  var a =  pos.x / DX - I;
  var b =  pos.y / DY - J;
  //格子点の速度を線形補間
  vel.x = (1.0 - b) * ((1.0 - a) * velX[I][J] + a * velX[I+1][J]) + b * ((1.0 - a) * velX[I][J+1] + a * velX[I+1][J+1]);
  vel.y = (1.0 - b) * ((1.0 - a) * velY[I][J] + a * velY[I+1][J]) + b * ((1.0 - a) * velY[I][J+1] + a * velY[I+1][J+1]);
  return vel;
}

//---------------------------------------------------
//イベント処理
function onClickC_Size()
{
  canvas.width = form1.c_sizeX.value;
  canvas.height = form1.c_sizeY.value;
  display();
}

function onChangeData()
{
  onClickReset();
  initData();
}

function onDisplay()
{
  display();
}
function onClickScale()
{
  rect.scale = parseFloat(form2.scale.value);
  display();
}
//-------------------------------------------------------------
function onClickP()
{ 
  num0 = parseInt(form2.num0.value);
  period = parseFloat(form2.period.value);
  speedCoef = parseFloat(form2.speedCoef.value);
  sizeP= parseFloat(form2.sizeP.value);
  typeP= parseFloat(form2.typeP.value);
}

function onClickStart()
{
  fps = 0;
  elapseTime = 0;
  elapseTime0 = 0;
  elapseTime1 = 0;
  elapseTimeN = 0;
  elapseTimeN0 = 0;
  flagStart = true;
  flagStep = false;
  flagFreeze = false;
  lastTime = new Date().getTime();  
}

function onClickFreeze()
{
  flagStart = !flagStart;
  flagFreeze = !flagFreeze;
  
  flagStep = false;
}
function onClickStep()
{
  flagStep = true;
  flagStart = true;
  elapseTime = elapseTime0;
}
function onClickReset()
{
  elapseTime0 = 0;
  elapseTimeN0 = 0;
  flagStart = false;
  flagStep = false;
  initData();
  form1.e_time.value = "0";
  form1.n_time.value = "0";
  display();
}



