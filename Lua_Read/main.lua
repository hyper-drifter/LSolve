--testing getting array from fields module
fields = require "fields"

myArray = fields.getElectricFieldArray("LSolve-E-Output.tsv")

for i,v in ipairs(myArray) do
      for j,w in ipairs(v) do
            print(i.." "..j.." "..w[1].." "..w[2])
      end
end
