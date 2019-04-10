# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import create_reply as cre


class TestShirotan(unittest.TestCase):
    """test class of create_reply.py
    """

    def test_dict1(self):
        EXPECTED_REPLY = "海のなかだよーふーん"
        test_msgs = [
          "住所",
          "場所",
          "どこ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict2(self):
        EXPECTED_REPLY = "ぎょーざがだいすきなの おーしょーいきたいなあ"
        test_msgs = [
          "食べ物",
          "たべもの",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict3(self):
        EXPECTED_REPLY = "おはよーーしろたんだよ===="
        test_msgs = [
          "おはよう",
          "おはよー",
          "おはー",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict4(self):
        EXPECTED_REPLY = "こんにちわ!!!ーーしろたんだよ===="
        test_msgs = [
          "こんにちわ",
          "こんにちは",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict5(self):
        EXPECTED_REPLY = "Hello!! \"Im Shirotan\" Please call me \"TARO\"! "
        test_msgs = [
          "Hello",
          "hello",
          "Hi",
          "hi",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict6(self):
        EXPECTED_REPLY = "げんきだして\nぼくをもふもふしていいよ"
        test_msgs = [
          "疲れた",
          "つかれた",
          "つかれたー",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict7(self):
        EXPECTED_REPLY = "がめんのうえのほうにかいてあるよ↑↑"
        test_msgs = [
          "いまなんじ",
          "いま何時",
          "今何時",
          "今なんじ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict8(self):
        EXPECTED_REPLY = "おやすみーーねむーーねむーーー"
        test_msgs = [
          "おやすみ",
          "ねるね",
          "寝る",
          "オヤスミ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict9(self):
        EXPECTED_REPLY = "くちがわるいなぁ\nこれだからカンサイジンは"
        test_msgs = [
          "ぶっ殺す",
          "ぶっころ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict10(self):
        EXPECTED_REPLY = "ちーむしろたんの公式ぎゅうどんははよしのやだよー\nでもほんとーにすきなのはまつや☆"
        test_msgs = [
          "牛丼",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict11(self):
        EXPECTED_REPLY = "ちーむしろたんの公式どーなつはミスドだよー☆"
        test_msgs = [
          "ドーナッツ",
          "ドーナツ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict12(self):
        EXPECTED_REPLY = "ちーむしろたんの公式どりんくはスタバだよー☆"
        test_msgs = [
          "飲み物",
          "ドリンク",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict13(self):
        EXPECTED_REPLY = "ちーむしろたんの公式ぎょうざは・・・\nあー、おーしょーとみんみんでまようなー"
        test_msgs = [
          "餃子",
          "ぎょうざ",
          "ギョウザ",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict14(self):
        EXPECTED_REPLY = "ちーむしろたんの公式しゅーくりーむはビアードパパだよー☆"
        test_msgs = [
          "シュークリーム",
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY, cre.dictMsg(msg))

    def test_dict15(self):
        EXPECTED_REPLY = ["しろたんるーれっと",
                          "すたーと!!",
                          "じゃんがじゃんがじゃんが",
                          ["おうしょう", "なかう", "かつや", "よしのや", "おひつごはん",
                           "まつや", "イオンフードコート", "パスタ", "ココイチ", "くらずし",
                           "てんいち", "おおさかおうしょう", "ロイヤルホスト", "サイゼ", "ココス",
                           "やるき"],
                          "きみにきめた!"]
        test_msgs = [
            "今日なにたべよ"
        ]
        for msg in test_msgs:
            self.assertEqual(EXPECTED_REPLY[0], cre.dictMsg(msg)[0])
            self.assertEqual(EXPECTED_REPLY[1], cre.dictMsg(msg)[1])
            self.assertEqual(EXPECTED_REPLY[2], cre.dictMsg(msg)[2])
            self.assertIn(cre.dictMsg(msg)[3], EXPECTED_REPLY[3])
            self.assertEqual(EXPECTED_REPLY[4], cre.dictMsg(msg)[4])

    def test_dict_fix(self):
        EXPECTED_REPLY_LIST = [
            "ぼくしろたんむつかしいことはよくわからないし\nもちもちしたものがたべたいなあ",
            "ぼくしろたん",
            "ぽかぽかだねー",
            "おなかすいたなー",
            "おさんぽいこーっと",
        ]
        test_msgs = [
          "しね",
          "おまえなんてきらいだ",
          "東京ビックサイトはどっちですか?",
          "またねー",
          "しね",
          "おまえなんてきらいだ",
          "東京ビックサイトはどっちですか?",
          "またねー",
          "しね",
          "おまえなんてきらいだ",
          "東京ビックサイトはどっちですか?",
          "またねー",
          "しね",
          "おまえなんてきらいだ",
          "東京ビックサイトはどっちですか?",
          "またねー",
        ]
        for msg in test_msgs:
            self.assertIn(cre.dictMsg(msg), EXPECTED_REPLY_LIST)


if __name__ == "__main__":
    unittest.main()
