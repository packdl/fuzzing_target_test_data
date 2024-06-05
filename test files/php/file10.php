<?php

// Initiate the Upload
$ret = ftp_nb_put($ftp, "test.remote", "test.local", FTP_BINARY);
while ($ret == FTP_MOREDATA) {
   
   // Do whatever you want
   echo ".";

   // Continue uploading...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "There was an error uploading the file...";
   exit(1);
}
?>