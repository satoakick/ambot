require 'rest-client'
require 'json'
module Ruboty
  module Handlers
    class Say < Base
      on(
        /(?<remark>.*?)\z/,
        name: 'say',
        description: 'reply message'
      )

      def say(message)
        remark = message[:remark]
        #puts "message:: " + remark
        response = RestClient.get('http://localhost:8888/', {params: {'q' => remark}})
        json = JSON.parse(response)
        message.reply(json["output"])
      end
    end
  end
end
