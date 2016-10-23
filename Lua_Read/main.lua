--testing getting arrays from fields module

function love.load()
      length = 300
      height = 300
      love.window.setMode(300,300)

      fields = require "fields"
      potArray = fields.getPotentialFieldArray("Lua_Read/LSolve-V-output.tsv",300,300)

end

function love.update(dt)

end

function love.draw()

      --draws potential values as points. Blue for positive, red for negative. Magnitude expressed by color intensity
      for i=1,length do
            for j=1,height do
                  local color = potArray[i][j]
                  if color < 0 then
                        color = color * -1
                        love.graphics.setColor(color,0, 0, 255)
                  else
                        love.graphics.setColor(0,0, color, 255)
                  end
                  love.graphics.points(i,j)
            end
      end
end
