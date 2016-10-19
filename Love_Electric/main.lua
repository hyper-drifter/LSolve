--[[
     Author: Taylor Grubbs
     Type: Main Program
     Description: This program will read in electric field values from a tsv file and draw them in Love.
]]--
function love.load(arg)

     fields = require "fields"

     input = "Lua_Electric/LSolve-E-Output.tsv"

     myArray = fields.getElectricFieldArray(input)
     length, height = fields.getDimensions(input)

     love.window.setMode(length, height)

     magGrid = fields.getElectricFieldMagnitudes(myArray, length, height)


end

function love.update(dt)
     -- body...
end

function love.draw()

     --draws magnitudes as points
     for i=1,length do
          for j=1,height do
               local color = magGrid[i][j] * 30 --random 30 here to scale up values so that they are visible
               love.graphics.setColor(0,0,color,255)
               love.graphics.points(i, j)
          end
     end

end
