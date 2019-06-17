require 'pathname'
require 'fileutils'

=begin

file:         C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\voicememos.20190315_132810\2019-03\manage_voicememos.20190315_133842.rb

created at:   2019/03/15 13:39:24

<Usage>
C:\WORKS_2\WS\WS_Others\prog\D-5\1#\get_folder_list.rb

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\voicememos.20190315_132810\2019-03\
manage_voicememos.20190315_133842.rb

=end

################################
#	
#	vars (global)
#
################################
VERSION = "1.0"
FILE_PATH = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-5\\1#\\get_folder_list.rb"


################################
# @param
#   serial    20161221_141900
# @orig: C:\WORKS_2\WS\WS_Others\res.245\115\r.245-115.5#1.elec-conductivity.rb 
#
################################
def get_time_label(type = "serial")
  
  if type == "serial"
    
    #ref http://stackoverflow.com/questions/7415982/how-do-i-get-the-current-date-time-in-dd-mm-yyyy-hhmm-format
    return Time.now.strftime("%Y%m%d_%H%M%S")
    
  elsif type == "display"
    
    #ref http://stackoverflow.com/questions/7415982/how-do-i-get-the-current-date-time-in-dd-mm-yyyy-hhmm-format
    return Time.now.strftime("%Y/%m/%d  %H:%M:%S")
    
  else
    
    return Time.now.strftime("%Y%m%d_%H%M%S")
    
  end
  
end

def test_1
  
  
  ####################
  # step : A : 1
  #   prep
  ####################
  #ref https://stackoverflow.com/questions/6705982/escaping-single-and-double-quotes-in-a-string-in-ruby#6706040
  dpath_Src = %q[C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\voicememos.20190315_132810\2019-03]
  fname_Src = "data.dat"
  
  fpath_Src = "#{dpath_Src}\\#{fname_Src}"

  puts
  puts "[#{__FILE__} : #{__LINE__}] fpath_Src --> #{fpath_Src}" 
  
  ####################
  # step : A : 1.1
  #   validate
  ####################
  if File.exist?(fpath_Src)
  
    puts
    puts "[#{__FILE__} : #{__LINE__}] file --> exists" 
  
  else#if (File.exists?)
  
    puts
    puts "[#{__FILE__} : #{__LINE__}] file --> NOT exists"
    
    # exit
    return 
  
  end#if (File.exists?)

  ####################
  # step : A : 1.2
  #   validate : open file
  ####################
  #ref http://rubylearning.com/satishtalim/ruby_exceptions.html
  begin
    
    f_in = File.open(fpath_Src, "r")
#    f_in = File.open(fpath_Src + ".new", "r")
    
  rescue StandardError => e
    
    puts
    puts "[#{__FILE__} : #{__LINE__}] ERROR!"
    
    p e
    
    return
    
  end
  
#  f_in = File.open(fpath_Src + ".new", "r")
#  f_in = File.open(fpath_Src, "r")

  ####################
  # step : A : 1.3
  #   file : read lines
  ####################
#  lines = f_in.readlines
  #ref https://stackoverflow.com/questions/25168662/how-to-read-lines-from-file-into-array
  lines = File.readlines(fpath_Src)
  
  #debug
  puts
  puts "[#{__FILE__} : #{__LINE__}] lines --> #{lines.length.to_s}" 
  
  ####################
  # step : A : 2
  #   build : new lines
  ####################
  lines_New = []
    
  #ref https://stackoverflow.com/questions/20258086/difference-between-each-with-index-and-each-with-index-in-ruby#20258160
  lines.each_with_index do |val, idx|
    
    tokens = val.strip.split("\t")
#    tokens = val.split("\t")
    
    #debug
    puts
    puts "[#{__FILE__} : #{__LINE__}] iter (#{idx.to_s} : "
    p tokens
    puts
    
    strOf_TimeLabel = (tokens[0].split(".")[0]).split(" ").join("_")
    
#    puts "tokens"
#    p tokens
#    p strOf_TimeLabel
    
    val_New = "m=#{strOf_TimeLabel}.#{tokens[1]}.m4a"
    
    p val_New
    
#    # append
#    lines_New << val_New
    ####################
    # step : A : 2.1
    #   copy file
    ####################
    ####################
    # step : A : 2.1 : 1
    #   path : source
    ####################
    _fpath_Src = "#{dpath_Src}\\#{tokens[0]}"

    ####################
    # step : A : 2.1 : 2
    #   validate : exitsts
    ####################
    judge = File.exist?(_fpath_Src)
    
    if judge == false
    
      #debug
      puts
      puts "[#{__FILE__} : #{__LINE__}] file --> NOT exist : #{_fpath_Src}" 
    
    else#if (judge == false)
    
      #debug
      puts
      puts "[#{__FILE__} : #{__LINE__}] file --> exists : #{_fpath_Src}" 
      
    
    end#if (judge == false)
    
    ####################
    # step : A : 2.1 : 3
    #   dest file
    ####################
    _fpath_Dst = "#{dpath_Src}\\#{val_New}"
    
    ####################
    # step : A : 2.1 : 4
    #   copy
    ####################
    FileUtils.cp(_fpath_Src, _fpath_Dst)
    
  end
  
  puts
  p lines_New

#  ####################
#  # step : A : 3
#  #   new file
#  ####################
#  lines.each_with_index do |val, idx|
#    
#    ####################
#    # step : A : 3.1
#    #   build : fpath source
#    ####################
#    _fpath_Src = "#{dpath_Src}\\#{val}"
#    
#    ####################
#    # step : A : 3.2
#    #   validate : exitsts
#    ####################
#    judge = File.exist?(_fpath_Src)
#    
#    if judge == false
#    
#      #debug
#      puts
#      puts "[#{__FILE__} : #{__LINE__}] file --> NOT exist : #{_fpath_Src}" 
#    
#    else#if (judge == false)
#    
#      #debug
#      puts
#      puts "[#{__FILE__} : #{__LINE__}] file --> exists : #{_fpath_Src}" 
#      
#    
#    end#if (judge == false)
#    
#  end#lines.each_with_index do |val, idx|
  
  
  #_20190315_134150
  
  ####################
  # step : X : 1.1
  #   close : file
  ####################
  f_in.close
  
end#def test_1

def exec
  
  ####################
  # ops
  ####################
  test_1
  
  puts
  puts "[#{__FILE__} : #{__LINE__}] exec --> done" 

    
end#exec

exec
