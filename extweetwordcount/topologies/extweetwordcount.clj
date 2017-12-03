(ns extweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn extweetwordcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration
    {"parse-tweet-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["valid_words"]
          :p 2
          )
      "count-bolt" (python-bolt-spec
            options
            {"parse-tweet-bolt" ["valid_words"]}
            "bolts.wordcount.WordCounter"
            ["words" "count"]
            :p 2
            )
    }
  ]
)
