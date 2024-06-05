<?php
$formatter = IntlDateFormatter::create('es_ES',
        IntlDateFormatter::FULL,
        IntlDateFormatter::FULL,
        'Europe/Madrid');

$val = IntlCalendar::getNow();

var_dump($val);
echo $formatter->format(IntlCalendar::getNow() / 1000.), "\n";