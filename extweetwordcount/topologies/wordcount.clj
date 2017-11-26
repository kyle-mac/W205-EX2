(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; spout configuration
    {"word-spout" (python-spout-spec
          options
          "spouts.words.WordSpout"
          ["word"]
          )
    }
    ;; bolt configuration
    {"count-bolt" (python-bolt-spec
          options
          {"word-spout" :shuffle}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 2
          )
    }
  ]
)
