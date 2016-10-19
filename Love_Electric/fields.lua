--[[
      Name: fields.lua
      Type: Module
      Description: fields module for dealing with electric field output files
]]--
local fields = {}

function fields.getDimensions(filename)
      local inputFile = io.open(filename, "r")
      local length = inputFile:read("*number")
      local height = inputFile:read("*number")
      inputFile:close()
      return length, height
end

--reads electric field values from tsv file
function fields.getElectricFieldArray(filename)

      local inputFile = io.open(filename, "r")

      --reads length and width from file header
      local length = inputFile:read("*number")
      local height = inputFile:read("*number")

      --creates multidimensional-[x][y][2] array for storing field values
      local fieldGrid = {}
      for i=1,length do
            fieldGrid[i] = {}
            for j=1,height do
                  fieldGrid[i][j] = {}
            end
      end

      --gets those values
      while x ~= length or y ~= height do
            x = inputFile:read("*number")
            y = inputFile:read("*number")
            fieldGrid[x][y][1] = inputFile:read("*number")
            fieldGrid[x][y][2] = inputFile:read("*number")
      end

      inputFile:close()
      return fieldGrid
end


--gets electric field magnitudes from electric field grid
function fields.getElectricFieldMagnitudes(fieldGrid, length, height)

     --makes 2-D grid for field magnitudes
     local magGrid = {}
     for i=1,length do
           magGrid[i] = {}
     end

     --gets magnitudes
     for x=1,length do
          for y=1,height do
               magGrid[x][y] = math.sqrt(math.pow(fieldGrid[x][y][1], 2) + math.pow(fieldGrid[x][y][2], 2))
          end
     end

     return magGrid
end

return fields
