#INPUT="./make_inputs/*.txt"
INPUT="./dialogs/archives/*.txt"

File.open("input.txt", "w") do |input|
  Dir.glob("#{INPUT}").each do |f|
    File.open(f, "r:utf-8") do |_f|
      while line = _f.gets
        matched = line.match(%r{.+?「(.+?)」})
        if matched && matched[1]
          input.puts matched[1]
        end
      end
    end
  end
end
