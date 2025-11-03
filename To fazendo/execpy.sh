#!/bin/bash

codigo="ignora.py"

casos=1

for i in $(seq 1 $casos); do
   echo "Caso $i"
   python3 "$codigo" < "in$i.txt" > "myout$i.txt"
   diff "myout$i.txt" "out$i.txt"

   if [ $? -eq 0 ]; then
       echo "✅ Caso $i passou"
   else
       echo "❌ Caso $i falhou"
       echo "Esperado:"
       cat "out$i.txt"
       echo "Obtido:"
       cat "myout$i.txt"
   fi
   echo "----------------------"

done
