"""
    Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
    That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.


Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        """Returns the minimum number of substrings

        Args:
            s (str): Random string of characters

        Algorithm:
            Use two processes:  1) start by creating a partition with single char
                                2) start by creating as long of a partition as possible.

        Returns:
            int: Minumum number of substrings found
        """
        count = 0
        first_indx = 0
        last_indx = 1
        charSet = set()
        repeat_cntr = 0
        check_str = ""

        while True:



            # print(s[first_indx], s[last_indx])
            # last_indx += 1
            print(f'Current substring: {check_str}, Last Char is {s[last_indx-1:last_indx]}')
            print(f'First Indes: {first_indx}, Last Index is {last_indx}')

            if s[last_indx-1:last_indx] not in check_str:
                check_str += s[last_indx-1:last_indx]
                last_indx += 1

            else:
                last_indx -= 1
                if s[first_indx:last_indx] not in charSet:
                    charSet.add(s[first_indx:last_indx])
                    print(f"In First Loop, First Index is: {first_indx}, Last Index is: {last_indx}")
                elif s[first_indx:last_indx-1] not in charSet:
                    charSet.add(s[first_indx:last_indx-1])
                    last_indx -=1
                    print(f"In Second Loop, First Index is: {first_indx}, Last Index is: {last_indx}")
                else:
                    repeat_cntr += 1
                    print(f"Repeat Counter is: {repeat_cntr}")
                first_indx = last_indx
                last_indx +=1
                check_str = ""

            if first_indx >= len(s):

                if check_str not in charSet:
                    charSet.add(check_str)
                    print(f"Adding in: {check_str}")
                break

            print(f"Check String is: {check_str}")

            # else:
            #     print(f"Found dublicate at: {first_indx}, {last_indx}, String: {s[first_indx:last_indx]}")
            #     first_indx +=1
            #     last_indx +=1


            print(f'Char Set: {charSet}, Counter: {repeat_cntr}')
            # if s[first_indx:last_indx] not in partition_list:
            #     partition_list.append(s[first_indx:last_indx:last_indx])
            # if s[first_indx: last_indx]
        if "" in charSet:
                charSet.remove("")
        print(f"Counter {repeat_cntr}")
        return len(charSet) + repeat_cntr

# print(Solution().partitionString("axuzwxhwtrxaudbfecdagodjvyovokjfpnrecdypzrmdchgcdzmwgdfmnichtlttldfwumrzexkqhwkifiqsmqipuaacmjvysgiungrgwbzimdlmlbrkaziabwusryijthqslpqohdkifzwyyeaqqttmudbfrwguicbpjmwksqxveginxaoauypfkdtjmbvkcowkjisqajxfeiigpkhxilhphytykjmhhzcxdsrylmrfxevboxcmtbnwllcgzrpnyilnuidoydjisnietdxsdpeqgkphllzyaccxwingadfnilfprytsbmlimzlkbyscepbtdpnloegxssmytqqyttpriyjpnwnikviufqbgririqsjongvoslyxtlnkejimqbpjcvlnjfyqncirtqesisrscxtwhqbzueaobqzhkbepkvoampcqocjfljwcuhkoltwzdashpxhdwsiuijzgbciqwrmxdxwrnqhhzwqhbzvjboibegvytjacieucwjqifmhkpcwmjttlnzqvpyldiimshxzqlqvavdgriurvlyrwnvowyobprafqznijgmjwfkezpcaeczvvysqjelfvrxqrvqfxkclzvtmxxtealraoyctfogxdvdlfzvmdmpctplkkaxxvcsfitebxdzxftvuedojsxrzcyrgsoihsmfjvmasxhdpyjkthygnfvhyexujbqxgpcxphobklshkoorfupvufyudcejqitvedzdfaunujsbankcpevhkbzafhcfepulitogxtytrptorxinmwxuhrlvfrghujgxyzqlidfqwtulwkltbonrbggeqkiiugvjsxwwcxwfozswpmmcmpbadlglabavkiorcmdyfqmmyjekjydzoddsadhhcyjlrmqcxckqicxkwxgnffxulabiwqqjpjzpyghfxeumbbizptjmnfkuwliojhmcmbwrohjafflnlubjaiyghshouenwgkpfkfnrxziygtztrtacjkyyedwwcpkogtcenekdwibfielpswyhgadmbelgppmvlqyxecoruanrdpuxquebdumtkivcbaaypqoqecuuzksceijmarccrefqkcqhvapscqjmkqzmwkbnfmcmzxsjdgcmfekkfmjbkccrqhrcztkkczyfvuezvrtpnlklyhxdhdntsuuhvrploclujnthwttufwvbyqsloruvsdnywerqdqsoffoounqoumsugbaesbqhbxzuvpwvrbuhfrqjnbywqzaxkgzuoyczfprpewhfeqiachnnjmyvdtnioesvuyfnzuwtaclsaumdfpwokapqxkvvfpkasnxknghmuthcmzhiyeizajjklytaagcbonwukrwulcqsmbdypggciadxezatppksidnemriknylcwnyvaxtwmdmcfnrcomevzvzardfrxxijhdezskkjqnawczrlvcydtgxbekhoihdnnojqtwqkybdmwmcktjavdntpkelyigpafnkonqblusehejnfhovgjonibdaprhmvtytzfegpseyygmcohuqgsfrvtnmtntyuxjolwmryunuozrjgouakxvwtnqyznqtcgpxhpznvqgmchgxqyqgladtudfpuvngmmmqslxkmfpbkumegwlseqbbeazffthicvdpldihmvrbkpltkcfffrymezjlugrfctndqeezgemddbjcjsquygrapdritfthekupyrgjuacrspxuathquovfujgiammxoscontersxrzsndrjfiazrsgggjzkyqvlmmoayslwitlthrlxfetpmwonsikhwllsdhchgbsbvbxxvcfhsgzmtgkaeepdjckvuurreaypysfcqjbbdcpwndhqrwepgkshagvgxfuytjixpmnlhqafdnfksyjjbvhelosknwxvhpfvvgmfyqietwqaiwkrfiedziudinitqvzumpbaiqoxtfrincokwdvwfgtbjsmtyahfejceeonthjwfnietukvfprdtlcbkkqgznvwtplwigjpfdkhcguuuwzeltywtvbcjsotlgtomhimycpnmjeufzeaxuagsyfkzhehznewuflldsdpaybrndifbluvakvmbdwsevvsxfuvyrcradsetzjvzslfpmqjsytcswgdzmxekmgslwmdwhjhdmnkylkkvfvlrbzficgaegrekuxkbxvmvbfneoynjhrzeggbpbdgmxfgdcpytpmaqozhijocvpiinevfpbuutmmvwmqqbkqehoisptcwbdliurhzactlcdxfdwzbhzrrfuiulxvrnnubjptquhgwzcnegijrgdwcwweqrdzpjjqhuraiwqgunbmdymvnakgcbaelaefeyvmyvftapzrsxhynljvnyhgodvnbdoadadjvhjqazrztasetevtkpuwjpevogicjeeefcjuzlriifdiwptgmkraeuaiqdyhmxnezswhusuprfukaimfqfzfjspcxhuyfopjbmhstdjedoqupahdyeqmqmswnweiqdolvokydoilpzkkelrbguubykrzutyswcywjdqemxhhzcingsjqczhoyvfdiarjbjlyskgwejztowfgekjrazbvvauhrczaeesaxaxflarcsllzmmlxbeuniougzldgtkdvhlththihlgdjfthjfxbrfwirudipzqnrgebeixqpvyciinalxsjrtbrphgybzkjzwfgjpcwhhqktwzzlfewpvrjsbrxsgmbibvdhhuhwkkvylqbohxbdnlklljuququisemgvjuunhjivaijvbwvnvqjmnymjvyejpgeplfxieleaopkxmnkzsyuxetrsavpsawoirfyzjdsiurlnlpoaaixdfctlotyrshvzwukyqcfqrxylhajzcugvlubnetkatpbhphnoayjoxlbhbrxvyxudozkdcwavkpxcdwqiwgidiobvvjdabxlwednfwogcsnkixbkipkqtybacnmnaenarjflxjsyftkcgorvqakmkpllkvlgxkdvmmdklnxulxasfdvpvhdruckxhggumtszvqkfusrioiapvehmhvkyqhckmadcejawkpfwfxbtitiikxpjmsjsljqtvzjirysomhfctpiinxcqfawuxtwztebebqghuahrrkwvqtwcgpkejjtikisbrbhzdcpbbfkcwqlymzyxkmjpafdqmswfpgdeebrtmdnboonzabkthnwdslpibmqsttpqikinrttramqejmuyfxmbelklwafbxewnffggsrbsohpnxcbkdbxytuosfnemqalhdnhkgfnyuhdfaxpjjpshhbcgaehpwnxmieerolivijxavdzkspjmstrmurygmibhspotsoquqarqarmqkgngapyrtxbqglnfcyeglquxwmbekfopdtatdgumbbukuecmrgmrdhaszfmgpefoktdqyrxymlvzdyhwehhqnwmdizqlnjahchgssvvvvtuuvixtyfolnjeitwnwcgfsddswdryvljxqzmnfhpfozyxcduxgprfncmpzqlzlxeehzsqpqjyoavuiyiorfaxnpnypvnofuqzwtlckyezongiocgaifkxvrminqmvyshztnurnhlndmwtceizmzbajhnxphsulnugknfkeegwlnukgyotxlbvbdlbfedknyxqtygwmjqohnzleqfvafutvoukeuufqyhwzugwmeyhklflldqcbeneuvqtupqzmixfafnovwacedgbkooqzldwzfqpbtfutggqvwymrpdilytdvmannrljgfqyvwhdfxgcnslorvaovpobookhyyfdhogvktypyuvpkrzwlgdikomnengmawftvbrolxyzbuvzbqikjpkbzafhydlfqcyohtiqrzsqqsatcjcccjchhlbekufuzlhuaxnkslrryukomcsbmbawbzhnnfekpbwsfdzmhtjyxnvdssruhivwwkbtydpffftftznkracmopaatcbqubfzqkwzwmqqozhbkbdveqzwntclztodulyobknbonffxnidkdfuxdhumbpenwbasudnrkrlmonwokgldeazvyjejrulhdhbqsenbqzutoyjxfidkxprtijyjtvjywdzijakceouigulfiullgbnuzskldphonhjqkytamqdmnshobidhkxxktiqcxjtoenklexxagvqrhvlgoohuovbprtsooucnrcnactwgicnsjvadhjbclataloaufjldxjmbglerdhcswrdvvdhotqrbhkronxhtjbuppynwsodaqiilsgeoikyyubdxbdgucbmkfokzgedqojqcyjbtpvseercjvjosmknakngmttlwtwcpaxcgyrmqekgaflwptocbeyuuujaomnjzmmtwxshtimozuzrrjrjuveenakiksruufxchusrvhvtwmxjquvmjbabfmdyodrnrmgcoyhhoehiuthmpieqevmtynzxtaxopxqudmmtsgwusnkwhzilmxuwoxbsyfmarjzhnltzbnptlmgkoodsusebnspxwfgfvzsdjkhuhikpeinktwcafrdynhyztzuubonqzpojkxgseeugzedkztlrhmfklhweedcuouhxcudfqsxdetrkfjklggwpzmxofoukviqtsgszwailknenmzhxqpojymulrnxdtwnzrjyxgwhfpgllpoudfpwshlzwebsnskgxagaaadnshcuirrupeyohaxbicoofbuknavoerffmcailtepqcgyuhikcprixlmjzmazykwlusbmfccvoyhwduumtbzjvqvwgtpcezumzmppjurybgswtxbojoyljbxawxftyhzhresxzdqjtmkwekcxbezjtacrzeacrqtpsodoidmzjdjaklskbevcynxjdfoudthjbwbpifatokkcpuiawepngbczgdpaztontrsuddinmcprnqhbbbowffcpwqzmlcjbscamynmswjlbhmkbpumugrvinltfeejmtregjdmjdnunonraavrfxyihoigzvmicmwadydwxdicoauuuuakdoyqpchaonrwxflmqgsbgzzsjkhlgfjqahhfnrtteufrzywkgqcqbehpeveuwazlezdecpjfowftvqwyoixcwizvrekewgrkvmcmekrxzqfsoozfuvebhepxhtszdtpnlocwoorckgzbfqbkhuomvkiibvybklvcrjtffxiuiazvmpjtvowtttdmchyyleibtgzirqomqfswtrhdlkfuhffhckivoawpgslnxgvdlfdycafrkdgihkvdduycucvymflfakekltvtkwbmbyyvnlngspeqxkqpyrjjuckmkthbxipedchzdchgzpfdfiilidynainekjlpulewebuayrxbkqmdcbjqgjvrwbquhrawxqtzgkuqwopdqjdayxdqwzjrxvwyrfafncntvnqybhzcbfrtfiqdkafxyqehserxizcqcgriitnytofqdldjngrxdrpsckjhloimrlmyntfwppiqgnbewpgvwmrrwuvzfbdwpdapbcygfhgylvezlgkstiaxnhnnvudyhkpycivbbgqtzxlquqmcczurbzatlhrurteeqsfbigmebmooaopyycoscenawcotuiedylbnciykprxttmakbhxfpykvrmpxetxdkornkjeskqwsypsiwqhegzdcoyivuvzgaxfsbejpizkwisjsndfarbychhgbfdhgyotuafusjcpzrwpxexujkvooligzpfpvepymjdjzzmwrqeuuqyzamhflqhvvocngtdlocloplxxuxbvlewsbhzqfftsmfcrfxqqcxmghuzmdgigwhgrahvgabsfsudcfodroromalnsbuciomayksrjmifkdixnchpxpyttmhiqkxycwmbdjisigmqgrwnnhujshxyipvdptbdbsuarlgossnirardnjkubhaokljyxlyumzewxwjnveuhnrwopdxopxmwbqxashemarvmtuvoianaqojlfgkizrrirpqoxlwzwyhwgzlpzvptwsuoscmbabgypivvvcszyenrzeqnsujhfmqektxqckjhahbguhopfwftpmoaxdjbcscoliejwlhfuehjpzsxxssfpwtnqtfwpqfvopgboorjslgpklkqbcsduewvucsqrvathrouz"))

print(Solution().partitionString("ss"))
