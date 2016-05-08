Bundler.require

require 'nokogiri'
require 'anemone'

URL="http://example.com/"
OUTPUT='./dialogs/'

def get_detail_id page
  page.doc.xpath("")
      .attribute("href")
      .text
      .match(/#{URL}(.+?)\.html/)[1]
end

options = {
  :delay => 1,
  :obey_robots_txt => true 
}

Anemone.crawl(URL, options) do |anemone|
 
  #anemone.skip_links_like /example_*/

  anemone.focus_crawl do |page|
    page.links.keep_if do |link|
      link.to_s.match(/archives/)
    end
  end

  inner_block = Proc.new do |node, f|
  end

  anemone.on_every_page do |page|
    detail_id = get_detail_id page
    file_name = "#{OUTPUT}#{detail_id}.txt"
    puts file_name
    File.open(file_name, "w") do |f|
      page.doc.xpath("").each do |node|
        inner_block.call(node, f)
      end

      page.doc.xpath("").each do |node|
        inner_block.call(node, f)
      end
    end
  end
end
