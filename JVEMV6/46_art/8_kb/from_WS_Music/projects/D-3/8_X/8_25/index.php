<?php
	//http://phpspot.net/php/pg%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%AA%E3%82%B9%E3%83%88%E3%82%92%E5%8F%96%E5%BE%97.html
	
// 	if ($dir = opendir("data/")) {
	if ($dir = opendir(".")) {
		
// 		$count = 0;
		
		$file_names = array();
		
		while (($file = readdir($dir)) !== false) {
			
// 			$count += 1;
			
			if ($file != "." && $file != "..") {
				
				array_push($file_names, $file);
				
// 				$count += 1;
				
// // 				echo "count=".$count;
// // 				$items = array($_SERVER['SERVER_NAME'], $_SERVER['PHP_SELF']);
// 				$items = array($_SERVER['PHP_SELF']);
				
// 				$link = join($items);
				
// // 				echo $count."."."<a href='".$link."'>"."$file"."</a>"."\n";
// 				echo $count."."."<a href='".$file."'>"."$file"."</a>"."\n";
				
// 				echo "<br/>";
			}
		}
		closedir($dir);

		// Sort names
		sort($file_names);
		
		// Show file names
		$count = 1;
		
		foreach ($file_names as $name) {
			
			echo $count.". "."<a href='".$name."'>"."$name"."</a>"."\n";
			echo "<br/>";
			
			$count += 1;
		}
		
	}//if ($dir = opendir("."))
	
	//echo "<br/>";
	//echo "Done";
	//echo `whoami`;
	
?>