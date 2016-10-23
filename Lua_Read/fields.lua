--[[
      Name: fields.lua
      Type: Module
      Description: fields module for dealing with electric field output files
]]--
local fields = {}

function fields.getDimensions(filename)
      local inputFile = io.open(filename, "r")
      length = inputFile:read("*number")
      height = inputFile:read("*number")
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

function fields.getPotentialFieldArray(filename, length, height)--need to input dimensions of array file

      local inputFile = io.open(filename, "r")
      local fieldGrid = {}
      for i=1,length do
            fieldGrid[i] = {}
      end

      for y=1,height do
            for x=1,length do
                  fieldGrid[x][y] = inputFile:read("*number")
            end
      end

      return fieldGrid
end

return fields
