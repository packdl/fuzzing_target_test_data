<?php

$image1 = new imagick("image1.png");
$image2 = new imagick("image2.png");

$result = $image1->compareImages($image2, Imagick::METRIC_MEANSQUAREERROR);
$result[0]->setImageFormat("png");

header("Content-Type: image/png");
echo $result[0];

?>