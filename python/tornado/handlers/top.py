# -*- coding: utf-8 -*-
from base import BaseHandler
from prediction import prediction
import json
import argparse
import urllib2
import cPickle as pickle
import settings

import logging
app_log = logging.getLogger("tornado")

class TopHandler(BaseHandler):

    vocabulary = settings.path(settings.ROOT, "models", "vocab.bin")
    model      = settings.path(settings.ROOT, "models", "charrnn_epoch.chainermodel")
    #print("vocabulary: "+ vocabulary)
    #print("model: "+model)
    VOCAB = pickle.load(open(vocabulary, 'rb'))
    MODEL = pickle.load(open(model, 'rb'))

    def get(self):

        query = self.get_argument("q", default="")
        #print("------------query: "+query)
        res = {
            "input": query,
            "output": ""
        }

        if query != "":
            parser = argparse.ArgumentParser()

            parser.add_argument('--seed',       type=int,   default=None)
            parser.add_argument('--sample',     type=int,   default=1)
            parser.add_argument('--primetext',  type=str,   default='')
            parser.add_argument('--length',     type=int,   default=2000)
            parser.add_argument('--gpu',        type=int,   default=-1)

            args = parser.parse_args([])

            args.primetext = query
            args.sample = 1
            args.length = 500
            output = prediction(args, vocab=self.VOCAB, model=self.MODEL)
            
            output_1 = output
            output_2 = output[len(query):]
            output_3 = output[len(query):].split("\n")
            ret = output[len(query):].split("\n")[0]
            #output = output[len(query):].lstrip("?\n").lstrip("？\n").lstrip("??\n").lstrip("？？\n").lstrip().split("\n\n")[0]

            #print("-------------output_1: ")
            #print(output_1)
            #print("-------------output_2: ")
            #print(output_2)
            #print("-------------output_3: ")
            #print(output_3)
            #print("-------------ret: ")
            #print(ret)


            res["output"] = ret

        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(
            json.dumps(res, ensure_ascii=False))
