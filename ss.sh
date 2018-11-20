#!/bin/bash

cat list.txt |while read line
do
cat $line >>model.prototxt
done
