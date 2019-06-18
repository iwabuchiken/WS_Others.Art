=begin

pushd C:\WORKS_2\WS\WS_Others\free\tools\
ruby modify_web_tables.rb

=end

#######################
#
# read data : http://fx.minkabu.jp/indicators/03018
#   1月  2月  3月  4月  5月  6月  7月  8月  9月  10月 11月 12月
#    2017年 -0.8  0.4   0.4 -0.1  0.0 -0.5  0.3 0.4      
#    2016年 -1.4  0.2 1.2 0.0   0.2 -0.6  0.1 0.4   -0.1  0.5
#    2015年 -1.6    1.1 0.2 0.2     0.0 0.2 0.1 -0.1  0.0
#    2014年 -1.1  0.3   0.2 -0.1  0.1 -0.7      0.0 -0.2  -0.1
#    2013年 -1.0  0.4       0.1 -0.5  0.1     -0.1  0.3
#    2012年                       0.4
#
#
#######################
def modify_tables_20171029_203847
  
  fpath = "../data/20171029_203821.dat"
  
  f = File.open(fpath)
  
  p f.readlines
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] file => opened : #{fpath}"
  
  
  f.close
  
end#modify_tables_20171029_203847

def exec

  modify_tables_20171029_203847
  
end

exec
