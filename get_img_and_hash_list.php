<?php

// This script is expected to be located at https://example.de/smartpanel/austausch/utils/get_img_and_hash_list.php
// Any new location of this script has to be integrated into the smartpanel

$directory = "/var/www/web12805/html/smartpanel/austausch/images";
// It is important to this script that the slideshow-images are in this directory or subdirectories of it.
// The directory should not end with a slash.
 
// define a function to recursively scan the directory and output the file paths with their hashes
function scan_directory($directory) {
    $dir_handle = opendir($directory);

    // loop through each file in the directory
    while (false !== ($file = readdir($dir_handle))) {
        // skip "." and ".." directories
        if ($file != "." && $file != "..") {
            $full_path = $directory . "/" . $file;

            // if the file is a directory, recursively scan it
            if (is_dir($full_path)) {
                scan_directory($full_path);
            }
            // if the file is a file, output its path and hash
            elseif (is_file($full_path)) {
                echo hash_file('sha256', $full_path) . "https://example.de" . str_replace("/var/www/web12805/html", "", $full_path) . "\n"; //The hash must not contain "http"
            }
        }
    }
    closedir($dir_handle);
}

scan_directory($directory);

?>
