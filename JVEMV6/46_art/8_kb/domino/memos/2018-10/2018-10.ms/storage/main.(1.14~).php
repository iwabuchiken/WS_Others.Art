<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

C:\WORKS_2\WS\WS_Others\free\
C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

/WS/WS_Others/free/UH8G6E_CE/

-->
<?php 

	require 'setup.php';
// 	require_once 'setup.php';

	/*******************************
		url
	*******************************/
	@$query_Url = $_GET['url'];
	
// 	echo "\$query_Url => '" . $query_Url . "'";

	if ($query_Url == null || $query_Url == '') {
	
		$query_Url = 'http://benfranklin.chips.jp/cake_apps/images/ifm11/2014-08-12_12-17-13_686.jpg';
	
	}//if ($query_Url == null || $query_Url == '')

	
?>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    
    <title><?php echo $session; ?> (<?php echo $version; ?>)</title>
<!--     <title>rect select</title> -->

	<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js">
		</script>
		
	<script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js">
		</script>
		
	<link rel="stylesheet" type="text/css" href="<?php echo $fpath_CSS; ?>" />

	<script type="text/javascript" src="<?php echo $fpath_JS; ?>">
		</script>
		
		
		
</head>
<body>

	
	<div id="div_message">
		
		<?php 
		
// 			echo "\$fpath_CSS : " . $fpath_CSS;
			
// 			echo "<br>"; 
			
// 			echo "\$fpath_JS_2" . $fpath_JS_2;
		
		?>
	
	</div><!-- <div id="div_message"> -->
	
    <div class="main">
<!--         <canvas id="drowing" class="drowing" width="300px" height="300px"></canvas> -->
<!--         <canvas id="drowing" class="drowing" width="50%" height="0"></canvas> -->
        <canvas id="drowing" class="drowing" width="0" height="0"></canvas>
    </div>

	<div>    
	    <input type="text" 
			 
			id="ipt_Image_File_URL"
			
			value="<?php echo $query_Url; ?>"
			>
	    
	    <button id="btn_Image_File_URL"
	    	onclick="get_Image();"
	    	>
	    	Go
	    </button>
	    
	    <span id="dflt_Image_Url" hidden><?php echo $query_Url; ?></span>
    </div>

    <div>
        <div>zキーで最新の矩形を削除</div>
    </div>

<hr>
    <?php 
    
    	require_once 'partials/main_controls.php';
    
    
    ?>


<hr>
    <br>
    <br>
    
    <?php 
    
    	require_once 'partials/link_to_session_root.php';
    
    
    ?>
    
</body>
</html>
