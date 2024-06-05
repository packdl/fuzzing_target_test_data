<?php

// Assuming $coll is a valid Collection object

// Extract all the documents from the Collection and group the results by the 'name' field
$res = $coll->find()->groupBy('name')->execute();

?>