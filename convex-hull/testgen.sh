#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p input
mkdir -p output

pushd $SCRIPT_DIR
    values=(
        '2,3'
        '3,3'
        '4,5'
        '5,10'
        '6,20'
        '7,40'
        '8,160'
        '9,500'
        '10,1000'
        '11,5000'
        '12,10000'
        '13,20000'
        '14,40000' 
        '15,100000'
        '16,200000'
        '17,400000'
        '18,600000'
        '19,800000'
        '20,1000000'
)

pushd solutions
popd

  for datarow in "${values[@]}"; do
    while IFS=',' read -r i n k;  do
      echo $i $n
      echo $n | python3 ./mkin.py > input/input$i.txt;
      #./solutions/solutioncpp < input/input$i.txt > output/output$i.txt
    done <<< "$datarow"
  done

  for i in {0..1}
  do
    #./solutions/solutioncpp < input/input$i.txt > output/output$i.txt
    python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
  done

rm -rf cases.zip
zip -r cases input output
popd
