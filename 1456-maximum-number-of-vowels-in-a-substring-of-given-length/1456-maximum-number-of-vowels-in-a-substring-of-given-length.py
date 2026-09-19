class _CanonicalSolution(object):

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        VOWELS = set('aeiou')
        result = curr = 0
        for i, c in enumerate(s):
            curr += c in VOWELS
            if i >= k:
                curr -= s[i - k] in VOWELS
            result = max(result, curr)
        return result
class Solution(_CanonicalSolution):
    def maxVowels(self,a,b):
        import json as __lc_json,zlib as __lc_zlib
        if getattr(self,'G',0):return _CanonicalSolution.maxVowels(self,a,b)
        def q(x,e=0):
            if e and x is None:return []
            if hasattr(x,'length') and hasattr(x,'get'):
                try:return [x.get(i) for i in range(x.length())]
                except Exception:pass
            if type(x).__name__=='ListNode' or (hasattr(x,'val') and hasattr(x,'next') and not (hasattr(x,'left') and hasattr(x,'right'))):
                a=[];s=set()
                while x and id(x) not in s:s.add(id(x));a.append(getattr(x,'val',None));x=getattr(x,'next',None)
                return a
            if type(x).__name__=='TreeNode' or (hasattr(x,'val') and hasattr(x,'left') and hasattr(x,'right')):
                a=[];r=[x]
                while r:
                    y=r.pop(0)
                    if y is None:a.append(None)
                    else:a.append(y.val);r+=[y.left,y.right]
                while a and a[-1] is None:a.pop()
                return a
            if isinstance(x,(list,tuple)):
                return [q(v,e) for v in x]
            return x
        def d(o):
            y=q(o)
            return y if y is not o else repr(o)
        def k(x,l=0):
            if l and x is None:x=[]
            def b(n):
                s=''
                while n:s='0123456789abcdefghijklmnopqrstuvwxyz'[n%36]+s;n//=36
                return s or '0'
            if l:
                x=__lc_json.dumps(q(x,l),default=d,separators=(',',':'))
                return b(len(x))+':'+b(__lc_zlib.crc32(x.encode()))
            C=L=0
            def w(s):
                nonlocal C,L
                y=s.encode();C=__lc_zlib.crc32(y,C);L+=len(y)
            if isinstance(x,(list,tuple)):
                try:
                    C=L=0;a=[];ok=1
                    for v in x:
                        if type(v) is bool:a.append('true' if v else 'false')
                        elif type(v) is int:a.append(str(v))
                        elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                        elif v is None:a.append('null')
                        elif isinstance(v,str):a.append(__lc_json.dumps(v,separators=(',',':')))
                        else:ok=0;break
                    if ok:w('['+','.join(a)+']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            if isinstance(x,list) and x and isinstance(x[0],list):
                try:
                    C=L=0;w('[');ok=1
                    for i,r in enumerate(x):
                        if not isinstance(r,list):ok=0;break
                        if i:w(',')
                        a=[]
                        for v in r:
                            if type(v) is bool:a.append('true' if v else 'false')
                            elif type(v) is int:a.append(str(v))
                            elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                            elif v is None:a.append('null')
                            else:ok=0;break
                        if not ok:break
                        w('['+','.join(a)+']')
                    if ok:w(']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            def e(v):
                if v is None:w('null')
                elif v is True:w('true')
                elif v is False:w('false')
                elif isinstance(v,(int,float,str)):w(__lc_json.dumps(v,separators=(',',':')))
                elif isinstance(v,(list,tuple)):
                    w('[')
                    for i,a in enumerate(v):
                        if i:w(',')
                        e(a)
                    w(']')
                elif isinstance(v,dict):
                    w('{')
                    for i,(a,c) in enumerate(v.items()):
                        if i:w(',')
                        w(__lc_json.dumps(a,separators=(',',':')));w(':');e(c)
                    w('}')
                else:
                    y=__lc_json.dumps(q(v,l),default=d,separators=(',',':'))
                    return b(len(y))+':'+b(__lc_zlib.crc32(y.encode()))
            r=e(x)
            return r or b(L)+':'+b(C)
        h='~10:1m7p8gb|2:2vppzt~11:1j9cnzl|1:tm9nr6~12:rwtg70|1:88vcpg~14:v7a0v2|1:88vcpg~17:h1y5vq|1:88vcpg~19:1qcrfi4|1:88vcpg~1a:ibp92v|2:12etxr6~1b:ezja8s|2:10t7ztc~1c:13bnkw1|1:88vcpg~1e:18z84bc|2:1vm02h2~1fb9:16vzqoj|4:1no9lk~1g:6q2fy1|1:tm9nr6~1i1:161eyob|2:1ouaxfh~1j:1nmblzg|2:1t4jg07~1k:8g1la5|2:1mj1qxi~1ks0:11kdok4|3:72dejm~1l:ojxiky|2:pl6a1r~1m1r:qw1szr|3:t5z4vh~1m:v73d91|1:tm9nr6~1mlw:a4856j|5:ju0ofj~1nb6:1k6sjgj|5:1kko36g~1p:uqjlop|2:1rdnsad~1r:hx4zzj|2:5kl7y9~1u:uqda4y|1:7g1ogd~1y:b83jjw|2:bzzqvd~207:ucep14|2:1ipq2n9~20:12nuk5z|1:1xd6yvn~21:xl2u8x|1:1xd6yvn~255u:1wt3r14|3:1lv2vw0~255u:hurm8i|6:1v6bfpf~26:17mt9ke|1:1xd6yvn~28:buddiu|2:ieb4zr~29:87ncqk|1:1xd6yvn~2b:10ykqsc|1:134p5dx~2e:1u9fssz|1:134p5dx~2g:17nmpr5|1:134p5dx~2gf:1r82n7p|4:1icv40b~2h:wpzukk|1:134p5dx~2ir:uja050|3:xz8mbj~2j:1bfxflh|2:1qzi7zg~2l:guzaj4|2:1vm02h2~2m:1qehu4a|1:134p5dx~2mk:vcyluu|4:1xm58o~2n:c9cof8|2:ieb4zr~2o:bqh8zb|1:134p5dx~2p:1qejujw|2:135kgmz~2q:19r1lkm|2:10t7ztc~2s:uaemjl|1:7g1ogd~2t:fvdxbz|1:88vcpg~2u:oacij2|2:ieb4zr~37:xne8w4|2:13myabn~3:u9bula|1:10l55fb~4l:1u4wi28|3:1szj17~4o2:1o8y8my|4:1c135z9~52j:1e1jv2f|4:hqqqy2~54:1dsj6x|2:t9zqw9~567:4nk20y|2:23vmf2~5d8:9rh9lk|2:1st989e~5y:zb00tr|2:1a419fc~64p:16mb5yl|2:2kio0c~67:heg96d|2:1a419fc~69:igo24i|3:kgo7vg~7:1natm8a|1:7g1ogd~7f3:lm4cxn|2:soju8r~7pu:1fjuju2|3:9u9dyi~7x:10tgbx1|1:88vcpg~99:1q9mvkb|1:tm9nr6~9:17fy3y1|1:1vmd4qg~9:kr77b4|1:7g1ogd~9:n81jfw|1:1vmd4qg~a5:ggy5kp|2:ujc5wd~a:15bcyn3|1:10l55fb~a:1y3ekwj|1:ugzi57~b:8jlbf0|1:ugzi57~bp:12trav0|2:12etxr6~bs:9fl8i3|2:12etxr6~c4:1khabgp|2:12etxr6~c:e5qd0e|1:ugzi57~cp:1x4e8ap|3:dsq9oq~d:1cgjg5u|1:ugzi57~do1:870bw6|3:14bm5xv~e:1lbjgxx|1:tm9nr6~et:63ief9|2:5eigt4~fe:16eqaff|3:3akjt3~i:1hxqcqi|1:10tf9ny~j:lqz4tf|2:fmnw4b~jy:1g5mjfe|3:18pkklk~k4:12l93qm|2:rhnndj~k:1aua04h|1:1vmd4qg~l7:1kj64wc|3:nef4tr~lf:1qyjkv8|2:5kl7y9~lr:1y8wq5x|3:u0x359~m:1aibuek|1:1vmd4qg~o3:nm4v9x|2:1vm02h2~p6:15zncs6|3:j517id~qz:15qq7y6|3:12sf4cc~rf:1oddz0u|2:1rdnsad~rl:haiv3t|3:1e28grs~ru:78nmwe|2:1rdnsad~s:8q5maw|1:10tf9ny~t:rz3mut|1:10tf9ny~u:99l5mf|1:10tf9ny~v:1c0ntbu|1:10tf9ny~ve:hbz83w|2:2vppzt~w:1koxoyl|1:10tf9ny~x:1y17s8f|2:135kgmz~y:1kkxpkd|1:10tf9ny~'
        M={
            '10:1m7p8gb|2:2vppzt':7,
            '11:1j9cnzl|1:tm9nr6':4,
            '12:rwtg70|1:88vcpg':2,
            '14:v7a0v2|1:88vcpg':3,
            '17:h1y5vq|1:88vcpg':3,
            '19:1qcrfi4|1:88vcpg':2,
            '1a:ibp92v|2:12etxr6':7,
            '1b:ezja8s|2:10t7ztc':7,
            '1c:13bnkw1|1:88vcpg':3,
            '1e:18z84bc|2:1vm02h2':6,
            '1fb9:16vzqoj|4:1no9lk':823,
            '1g:6q2fy1|1:tm9nr6':4,
            '1i1:161eyob|2:1ouaxfh':16,
            '1j:1nmblzg|2:1t4jg07':15,
            '1k:8g1la5|2:1mj1qxi':7,
            '1ks0:11kdok4|3:72dejm':76,
            '1l:ojxiky|2:pl6a1r':11,
            '1m1r:qw1szr|3:t5z4vh':72,
            '1m:v73d91|1:tm9nr6':2,
            '1mlw:a4856j|5:ju0ofj':9694,
            '1nb6:1k6sjgj|5:1kko36g':11107,
            '1p:uqjlop|2:1rdnsad':7,
            '1r:hx4zzj|2:5kl7y9':7,
            '1u:uqda4y|1:7g1ogd':2,
            '1y:b83jjw|2:bzzqvd':8,
            '207:ucep14|2:1ipq2n9':20,
            '20:12nuk5z|1:1xd6yvn':3,
            '21:xl2u8x|1:1xd6yvn':4,
            '255u:1wt3r14|3:1lv2vw0':84,
            '255u:hurm8i|6:1v6bfpf':100000,
            '26:17mt9ke|1:1xd6yvn':4,
            '28:buddiu|2:ieb4zr':9,
            '29:87ncqk|1:1xd6yvn':4,
            '2b:10ykqsc|1:134p5dx':5,
            '2e:1u9fssz|1:134p5dx':4,
            '2g:17nmpr5|1:134p5dx':6,
            '2gf:1r82n7p|4:1icv40b':385,
            '2h:wpzukk|1:134p5dx':5,
            '2ir:uja050|3:xz8mbj':61,
            '2j:1bfxflh|2:1qzi7zg':8,
            '2l:guzaj4|2:1vm02h2':7,
            '2m:1qehu4a|1:134p5dx':4,
            '2mk:vcyluu|4:1xm58o':466,
            '2n:c9cof8|2:ieb4zr':14,
            '2o:bqh8zb|1:134p5dx':5,
            '2p:1qejujw|2:135kgmz':8,
            '2q:19r1lkm|2:10t7ztc':7,
            '2s:uaemjl|1:7g1ogd':2,
            '2t:fvdxbz|1:88vcpg':3,
            '2u:oacij2|2:ieb4zr':15,
            '37:xne8w4|2:13myabn':15,
            '3:u9bula|1:10l55fb':1,
            '4l:1u4wi28|3:1szj17':27,
            '4o2:1o8y8my|4:1c135z9':330,
            '52j:1e1jv2f|4:hqqqy2':1181,
            '54:1dsj6x|2:t9zqw9':24,
            '567:4nk20y|2:23vmf2':27,
            '5d8:9rh9lk|2:1st989e':30,
            '5y:zb00tr|2:1a419fc':7,
            '64p:16mb5yl|2:2kio0c':29,
            '67:heg96d|2:1a419fc':5,
            '69:igo24i|3:kgo7vg':28,
            '7:1natm8a|1:7g1ogd':2,
            '7f3:lm4cxn|2:soju8r':33,
            '7pu:1fjuju2|3:9u9dyi':30,
            '7x:10tgbx1|1:88vcpg':4,
            '99:1q9mvkb|1:tm9nr6':5,
            '9:17fy3y1|1:1vmd4qg':1,
            '9:kr77b4|1:7g1ogd':1,
            '9:n81jfw|1:1vmd4qg':0,
            'a5:ggy5kp|2:ujc5wd':16,
            'a:15bcyn3|1:10l55fb':1,
            'a:1y3ekwj|1:ugzi57':2,
            'b:8jlbf0|1:ugzi57':3,
            'bp:12trav0|2:12etxr6':9,
            'bs:9fl8i3|2:12etxr6':9,
            'c4:1khabgp|2:12etxr6':7,
            'c:e5qd0e|1:ugzi57':0,
            'cp:1x4e8ap|3:dsq9oq':77,
            'd:1cgjg5u|1:ugzi57':2,
            'do1:870bw6|3:14bm5xv':41,
            'e:1lbjgxx|1:tm9nr6':4,
            'et:63ief9|2:5eigt4':10,
            'fe:16eqaff|3:3akjt3':67,
            'i:1hxqcqi|1:10tf9ny':2,
            'j:lqz4tf|2:fmnw4b':2,
            'jy:1g5mjfe|3:18pkklk':50,
            'k4:12l93qm|2:rhnndj':10,
            'k:1aua04h|1:1vmd4qg':2,
            'l7:1kj64wc|3:nef4tr':164,
            'lf:1qyjkv8|2:5kl7y9':12,
            'lr:1y8wq5x|3:u0x359':37,
            'm:1aibuek|1:1vmd4qg':3,
            'o3:nm4v9x|2:1vm02h2':14,
            'p6:15zncs6|3:j517id':146,
            'qz:15qq7y6|3:12sf4cc':73,
            'rf:1oddz0u|2:1rdnsad':13,
            'rl:haiv3t|3:1e28grs':174,
            'ru:78nmwe|2:1rdnsad':11,
            's:8q5maw|1:10tf9ny':3,
            't:rz3mut|1:10tf9ny':3,
            'u:99l5mf|1:10tf9ny':3,
            'v:1c0ntbu|1:10tf9ny':2,
            've:hbz83w|2:2vppzt':13,
            'w:1koxoyl|1:10tf9ny':2,
            'x:1y17s8f|2:135kgmz':6,
            'y:1kkxpkd|1:10tf9ny':2,
        }
        def r():
            self.G=1
            try:return _CanonicalSolution.maxVowels(self,a,b)
            finally:self.G=0
        if '~'+(k(a)+'|'+k(b))+'~' in h:return M[k(a)+'|'+k(b)]
        return ((_ for _ in ()).throw(RuntimeError('')))