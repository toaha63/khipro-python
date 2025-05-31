
# Define the mapping dictionaries for Bengali characters

# Dictionary for full vowel letters
vowels = {
    'o': 'অ',
    'a': 'আ',
    'i': 'ই',
    'ii': 'ঈ',
    'u': 'উ',
    'uu': 'ঊ',
    'q': 'ঋ',
    'e': 'এ',
    'oi': 'ঐ',
    'w': 'ও',
    'ou': 'ঔ',
    'ae': 'অ্যা',
    'wa': 'ওয়া',
    'we': 'ওয়ে',
    'wae': 'ওয়্যা',
    'fo': '',
    'fa': 'া',
    'fi': 'ি',
    'fii': 'ী',
    'fu': 'ু',
    'fuu': 'ূ',
    'fq': 'ৃ',
    'fe': 'ে',
    'foi': 'ৈ',
    'fw': 'ো',
    'fou': 'ৌ',
    'fae': '্যা',
    'fwa': 'োয়া',
    'fwe': 'োয়ে',
    'fwae': 'ওয়্যা'
}

# Dictionary for vowel signs (diacritics) used after consonants
vowel_signs = {
    'o': '',
    'a': 'া',
    'i': 'ি',
    'ii': 'ী',
    'u': 'ু',
    'uu': 'ূ',
    'uuff': '‌ূ',
    'q': 'ৃ',
    'qff': '‌ৃ',
    'e': 'ে',
    'oi': 'ৈ',
    'w': 'ো',
    'ou': 'ৌ',
    'ae': '্যা',
    'wa': 'োয়া',
    'we': 'োয়ে',
    'wae': 'ওয়্যা',
    'of': 'অ',
    'af': 'আ',
    'if': 'ই',
    'iif': 'ঈ',
    'uf': 'উ',
    'uuf': 'ঊ',
    'qf': 'ঋ',
    'ef': 'এ',

    'wf': 'ও',

    'aef': 'অ্যা',
    'waf': 'ওয়া',
    'wef': 'ওয়ে',
    'waef': 'ওয়্যা'
}

# Dictionary for consonants
consonants = {
    'k': 'ক',   # "k" maps to the Bengali consonant "ক"
    'kh': 'খ',  # "kh" maps to "খ"
    'g': 'গ',   # "g" maps to "গ"
    'gh': 'ঘ',  # "gh" maps to "ঘ"
    'ngf': 'ঙ',   # "ngf" maps to "ঙ"
    'c': 'চ',
    'ch': 'ছ',
    'j': 'জ',
    'jh': 'ঝ',
    'nff': 'ঞ', # this mapping will rarely be needed. ঞ is conjunct most of the time. Where it has shorter ways to be typed.
    'tf': 'ট',
    'thf': 'ঠ',
    'df': 'ড',
    'dhf': 'ঢ',
    'nf': 'ণ',
    't': 'ত',
    'th': 'থ',
    'd': 'দ',
    'dh': 'ধ',
    'n': 'ন',
    'p': 'প',
    'ph': 'ফ',
    'b': 'ব',
    'v': 'ভ',
    'm': 'ম',
#    'z': 'য', # we have added these 2 letters in phola
 #   'r': 'র',
    'l': 'ল',
    's': 'স',
    'sh': 'শ',
    'sf': 'ষ',
    'h': 'হ',
    'rf': 'ড়',
    'rff': 'ঢ়',
    'y': 'য়'


    # Additional consonant mappings can be added here
}

# Dictionary for conjuncts (combined consonant forms)
conjuncts = {
    'ry': 'র‌্য',
    'kk': 'ক্ক',
    'ktf': 'ক্ট',
    'ktfr': 'ক্ট্র',
    'kt': 'ক্ত',
    'ktr': 'ক্ত্র',
    'kb': 'ক্ব',
    'km': 'ক্ম',
    'kz': 'ক্য',
    'kr': 'ক্র',
    'kl': 'ক্ল',
    'kf': 'ক্ষ',
    'ksf': 'ক্ষ',
    'kkh': 'ক্ষ',
    'kfnf': 'ক্ষ্ণ',
    'kfn': 'ক্ষ্ণ',
    'ksfnf': 'ক্ষ্ণ',
    'ksfn': 'ক্ষ্ণ',
    'kkhn': 'ক্ষ্ণ',
    'kkhnf': 'ক্ষ্ণ',
    'kfb': 'ক্ষ্ব',
    'ksfb': 'ক্ষ্ব',
    'kkhb': 'ক্ষ্ব',
    'kfm': 'ক্ষ্ম',
    'kkhm': 'ক্ষ্ম',
    'ksfm': 'ক্ষ্ম',
    'kfz': 'ক্ষ্য',
    'ksfz': 'ক্ষ্য',
    'kkhz': 'ক্ষ্য',
    'ks': 'ক্স',
    'khz': 'খ্য',
    'khr': 'খ্র',
    'ggg': 'গ্গ',
    'gnf': 'গ্‌ণ',
    'gdh': 'গ্ধ',
    'gdhz': 'গ্ধ্য',
    'gdhr': 'গ্ধ্র',
    'gn': 'গ্ন',
    'gnz': 'গ্ন্য',
    'gb': 'গ্ব',
    'gm': 'গ্ম',
    'gz': 'গ্য',
    'gr': 'গ্র',
    'grz': 'গ্র্য',
    'gl': 'গ্ল',
    'ghn': 'ঘ্ন',
    'ghr': 'ঘ্র',
    'ngk': 'ঙ্ক',
    'ngkt': 'ঙ্‌ক্ত',
    'ngkz': 'ঙ্ক্য',
    'ngkr': 'ঙ্ক্র',
    'ngkkh': 'ঙ্ক্ষ',
    'ngksf': 'ঙ্ক্ষ',
    'ngkh': 'ঙ্খ',
    'ngg': 'ঙ্গ',
    'nggz': 'ঙ্গ্য',
    'nggh': 'ঙ্ঘ',
    'ngghz': 'ঙ্ঘ্য',
    'ngghr': 'ঙ্ঘ্র',
    'ngm': 'ঙ্ম',
    'cc': 'চ্চ',
    'cch': 'চ্ছ',
    'cchb': 'চ্ছ্ব',
    'cchr': 'চ্ছ্র',
    'cnff': 'চ্ঞ',
    'cb': 'চ্ব',
    'cz': 'চ্য',
    'jj': 'জ্জ',
    'jjb': 'জ্জ্ব',
    'jjh': 'জ্ঝ',
    'jnff': 'জ্ঞ',
    'gg': 'জ্ঞ',
    'jb': 'জ্ব',
    'jz': 'জ্য',
    'jr': 'জ্র',
    'nc': 'ঞ্চ',
    'nffc': 'ঞ্চ',
    'nj': 'ঞ্জ',
    'nffj': 'ঞ্জ',
    'njh': 'ঞ্ঝ',
    'nffjh': 'ঞ্ঝ',
    'nch': 'ঞ্ছ',
    'nffch': 'ঞ্ছ',
    'ttf': 'ট্ট',
    'tftf': 'ট্ট',
    'tfb': 'ট্ব',
    'tfm': 'ট্ম',
    'tfz': 'ট্য',
    'tfr': 'ট্র',
    'ddf': 'ড্ড',
    'dfdf': 'ড্ড',
    'dfb': 'ড্ব',
    'dfz': 'ড্য',
    'dfr': 'ড্র',
    'rfg': 'ড়্‌গ',
    'dhfz': 'ঢ্য',
    'dhfr': 'ঢ্র',
    'nftf': 'ণ্ট',
    'nfthf': 'ণ্ঠ',
    'nfthfz': 'ণ্ঠ্য',
    'nfdf': 'ণ্ড',
    'nfdfz': 'ণ্ড্য',
    'nfdfr': 'ণ্ড্র',
    'nfdhf': 'ণ্ঢ',
    'nfnf': 'ণ্ণ',
    'nfn': 'ণ্ণ',
    'nfb': 'ণ্ব',
    'nfm': 'ণ্ম',
    'nfz': 'ণ্য',
    'tt': 'ত্ত',
    'ttb': 'ত্ত্ব',
    'ttz': 'ত্ত্য',
    'tth': 'ত্থ',
    'tn': 'ত্ন',
    'tb': 'ত্ব',
    'tm': 'ত্ম',
    'tmz': 'ত্ম্য',
    'tz': 'ত্য',
    'tr': 'ত্র',
    'trz': 'ত্র্য',
    'thb': 'থ্ব',
    'thz': 'থ্য',
    'thr': 'থ্র',
    'dg': 'দ্‌গ',
    'dgh': 'দ্‌ঘ',
    'dd': 'দ্দ',
    'ddb': 'দ্দ্ব',
    'ddh': 'দ্ধ',
    'db': 'দ্ব',
    'dv': 'দ্ভ',
    'dvr': 'দ্ভ্র',
    'dm': 'দ্ম',
    'dz': 'দ্য',
    'dr': 'দ্র',
    'drz': 'দ্র্য',
    'dhn': 'ধ্ন',
    'dhb': 'ধ্ব',
    'dhm': 'ধ্ম',
    'dhz': 'ধ্য',
    'dhr': 'ধ্র',
    'ntf': 'ন্ট',
    'ntfr': 'ন্ট্র',
    'nthf': 'ন্ঠ',
    'ndf': 'ন্ড',
    'ndfr': 'ন্ড্র',
    'nt': 'ন্ত',
    'ntb': 'ন্ত্ব',
    'ntr': 'ন্ত্র',
    'ntrz': 'ন্ত্র্য',
    'nth': 'ন্থ',
    'nthr': 'ন্থ্র',
    'nd': 'ন্দ',
    'ndb': 'ন্দ্ব',
    'ndz': 'ন্দ্য',
    'ndr': 'ন্দ্র',
    'ndh': 'ন্ধ',
    'ndhz': 'ন্ধ্য',
    'ndhr': 'ন্ধ্র',
    'nn': 'ন্ন',
    'nb': 'ন্ব',
    'nm': 'ন্ম',
    'nz': 'ন্য',
    'ns': 'ন্স',
    'ptf': 'প্ট',
    'pt': 'প্ত',
    'pn': 'প্ন',
    'pp': 'প্প',
    'pz': 'প্য',
    'pr': 'প্র',
    'pl': 'প্ল',
    'ps': 'প্স',
    'phr': 'ফ্র',
    'phl': 'ফ্ল',
    'bj': 'ব্জ',
    'bd': 'ব্দ',
    'bdh': 'ব্ধ',
    'bb': 'ব্ব',
    'bz': 'ব্য',
    'br': 'ব্র',
    'bl': 'ব্ল',
    'vb': 'ভ্ব',
    'vz': 'ভ্য',
    'vr': 'ভ্র',
    'vl': 'ভ্ল',
    'mn': 'ম্ন',
    'mp': 'ম্প',
    'mpr': 'ম্প্র',
    'mph': 'ম্ফ',
    'mb': 'ম্ব',
    'mbr': 'ম্ব্র',
    'mv': 'ম্ভ',
    'mvr': 'ম্ভ্র',
    'mm': 'ম্ম',
    'mz': 'ম্য',
    'mr': 'ম্র',
    'ml': 'ম্ল',
    'zz': 'য্য',
    'lk': 'ল্ক',
    'lkz': 'ল্ক্য',
    'lg': 'ল্গ',
    'ltf': 'ল্ট',
    'ldf': 'ল্ড',
    'lp': 'ল্প',
    'lph': 'ল্ফ',
    'lb': 'ল্ব',
    'lv': 'ল্‌ভ',
    'lm': 'ল্ম',
    'lz': 'ল্য',
    'll': 'ল্ল',
    'shc': 'শ্চ',
    'shch': 'শ্ছ',
    'shn': 'শ্ন',
    'shb': 'শ্ব',
    'shm': 'শ্ম',
    'shz': 'শ্য',
    'shr': 'শ্র',
    'shl': 'শ্ল',
    'sfk': 'ষ্ক',
    'sfkr': 'ষ্ক্র',
    'sftf': 'ষ্ট',
    'sftfz': 'ষ্ট্য',
    'sftfr': 'ষ্ট্র',
    'sfthf': 'ষ্ঠ',
    'sfthfz': 'ষ্ঠ্য',
    'sfnf': 'ষ্ণ',
    'sfn': 'ষ্ণ',
    'sfp': 'ষ্প',
    'sfpr': 'ষ্প্র',
    'sfph': 'ষ্ফ',
    'sfb': 'ষ্ব',
    'sfm': 'ষ্ম',
    'sfz': 'ষ্য',
    'sk': 'স্ক',
    'skr': 'স্ক্র',
    'skh': 'স্খ',
    'stf': 'স্ট',
    'stfr': 'স্ট্র',
    'st': 'স্ত',
    'stb': 'স্ত্ব',
    'stz': 'স্ত্য',
    'str': 'স্ত্র',
    'sth': 'স্থ',
    'sthz': 'স্থ্য',
    'sn': 'স্ন',
    'sp': 'স্প',
    'spr': 'স্প্র',
    'spl': 'স্প্ল',
    'sph': 'স্ফ',
    'sb': 'স্ব',
    'sm': 'স্ম',
    'sz': 'স্য',
    'sr': 'স্র',
    'sl': 'স্ল',
    'hn': 'হ্ন',
    'hnf': 'হ্ণ',
    'hb': 'হ্ব',
    'hm': 'হ্ম',
    'hz': 'হ্য',
    'hr': 'হ্র',
    'hl': 'হ্ল',

    'ksh': 'কশ',
    'nsh': 'নশ',
    'psh': 'পশ',
    'ld': 'লদ',
    'gd': 'গদ',
    'ngkk': 'ঙ্কক',
    'ngks': 'ঙ্কস',
    'cn': 'চন',
    'cnf': 'চণ',
    'jn': 'জন',
    'jnf': 'জণ',
    'tft': 'টত',
    'dfd': 'ডদ',
    'nft': 'ণত',
    'nfd': 'ণদ',
    'lt': 'লত',
    'sft': 'ষত',
    'nfth': 'ণথ',
    'nfdh': 'ণধ',
    'sfth': 'ষথ',
    'ktfrf': 'ক্টড়',
    'ktfrff': 'ক্টঢ়',
    'kth': '',
    'ktrf': 'ক্তড়',
    'ktrff': 'ক্তঢ়',
    'krf': 'কড়',
    'krff': 'কঢ়',
    'khrf': 'খড়',
    'khrff': 'খঢ়',
    'gggh': 'জ্ঞঘ',
    'gdhf': 'গঢ',
    'gdhrf': 'গ্ধড়',
    'gdhrff': 'গ্ধঢ়',
    'grf': 'গড়',
    'grff': 'গঢ়',
    'ghrf': 'ঘড়',
    'ghrff': 'ঘঢ়',
    'ngkth': 'ঙ্কথ',
    'ngkrf': 'ঙ্কড়',
    'ngkrff': 'ঙ্কঢ়',
    'ngghrf': 'ঙ্ঘড়',
    'ngghrff': 'ঙ্ঘঢ়',
    'cchrf': 'চ্ছড়',
    'cchrff': 'চ্ছঢ়',
    'tfrf': 'টড়',
    'tfrff': 'টঢ়',
    'dfrf': 'ডড়',
    'dfrff': 'ডঢ়',
    'rfgh': 'ড়ঘ',
    'dhfrf': 'ঢড়',
    'dhfrff': 'ঢঢ়',
    'nfdfrf': 'ণ্ডড়',
    'nfdfrff': 'ণ্ডঢ়',
    'trf': 'তড়',
    'trff': 'তঢ়',
    'thrf': 'থড়',
    'thrff': 'থঢ়',
    'dvrf': 'দ্ভড়',
    'dvrff': 'দ্ভঢ়',
    'drf': 'দড়',
    'drff': 'দঢ়',
    'dhrf': 'ধড়',
    'dhrff': 'ধঢ়',
    'ntfrf': 'ন্টড়',
    'ntfrff': 'ন্টঢ়',
    'ndfrf': 'ন্ডড়',
    'ndfrff': 'ন্ডঢ়',
    'ntrf': 'ন্তড়',
    'ntrff': 'ন্তঢ়',
    'nthrf': 'ন্থড়',
    'nthrff': 'ন্থঢ়',
    'ndrf': 'ন্দড়',
    'ndrff': 'ন্দঢ়',
    'ndhrf': 'ন্ধড়',
    'ndhrff': 'ন্ধঢ়',
    'pth': 'পথ',
    'pph': 'পফ',
    'prf': 'পড়',
    'prff': 'পঢ়',
    'phrf': 'ফড়',
    'phrff': 'ফঢ়',
    'bjh': 'বঝ',
    'brf': 'বড়',
    'brff': 'বঢ়',
    'vrf': 'ভড়',
    'vrff': 'ভঢ়',
    'mprf': 'ম্পড়',
    'mprff': 'ম্পঢ়',
    'mbrf': 'ম্বড়',
    'mbrff': 'ম্বঢ়',
    'mvrf': 'ম্ভড়',
    'mvrff': 'ম্ভঢ়',
    'mrf': 'মড়',
    'mrff': 'মঢ়',
    'lkh': 'লখ',
    'lgh': 'লঘ',
    'shrf': 'শড়',
    'shrff': 'শঢ়',
    'sfkh': 'ষখ',
    'sfkrf': 'ষ্কড়',
    'sfkrff': 'ষ্কঢ়',
    'sftfrf': 'ষ্টড়',
    'sftfrff': 'ষ্টঢ়',
    'sfprf': 'ষ্পড়',
    'sfprff': 'ষ্পঢ়',
    'skrf': 'স্কড়',
    'skrff': 'স্কঢ়',
    'stfrf': 'স্টড়',
    'stfrff': 'স্টঢ়',
    'strf': 'স্তড়',
    'strff': 'স্তঢ়',
    'sprf': 'স্পড়',
    'sprff': 'স্পঢ়',
    'srf': 'সড়',
    'srff': 'সঢ়',
    'hrf': 'হড়',
    'hrff': 'হঢ়',
    'ldh': 'লধ',
    'ngksh': 'ঙ্কশ',
    'tfth': 'টথ',
    'dfdh': 'ডধ',
    'lth': 'লথ'

}

reph = {
    'rr': 'র্',
    'rae': 'র‌্যা'
}

phola = {
    'z': 'য',
    'r': 'র'
}

diacritics = {
    'ng': 'ং',
    'x': 'ঃ',
    'xx': '্‌',
    'qq': '্',
    '`': '‌',
    '``': '‍',
    'ngo': 'ঙ',
    'nga': 'ঙা',
    'ngi': 'ঙি',
    'ngii': 'ঙী',
    'ngu': 'ঙু',
    'nguu': 'ঙূ',
    'ngq': 'ঙৃ',
    'nge': 'ঙে',
    'ngoi': 'ঙৈ',
    'ngw': 'ঙো',
    'ngou': 'ঙৌ',
    'ngae': 'ঙ্যা',
    'ngwa': 'ঙোয়া',
    'ngwe': 'ঙোয়ে'

}

punctuations = {
    ';': '',
    ';;': ';',
    '.': '।',
    '..': '.',
    '...': '...'
}

digits = {
    '1': '১',
    '2': '২',
    '3': '৩',
    '4': '৪',
    '5': '৫',
    '6': '৬',
    '7': '৭',
    '8': '৮',
    '9': '৯',
    '0': '০',
    '.1': '.১',
    '.2': '.২',
    '.3': '.৩',
    '.4': '.৪',
    '.5': '.৫',
    '.6': '.৬',
    '.7': '.৭',
    '.8': '.৮',
    '.9': '.৯',
    '.0': '.০'
}

global_keys_list = list(vowels.keys()) + list(vowel_signs.keys()) + list(consonants.keys()) + list(conjuncts.keys()) + list(diacritics.keys()) + list(punctuations.keys()) + list(phola.keys()) + list(reph.keys()) + list(digits.keys())

# A simple tokenizer function that splits the input text into tokens
def tokenize(text):
    tokens = []  # Create an empty list to store tokens
    # Determine the maximum length among all mapping keys
    max_token_length = max(len(key) for key in global_keys_list)
    i = 0        # Initialize index at the start of the text
    while i < len(text):
        matched = False  # Flag to indicate if a token was found
        # Try from the longest possible token down to 1 character
        for l in range(max_token_length, 0, -1):
            # Ensure we don't exceed the string length
            if i + l <= len(text) and text[i:i+l] in global_keys_list:
                tokens.append(text[i:i+l])
                i += l  # Skip ahead by the length of the matched token
                matched = True
                break  # Exit the for loop once a match is found
        if not matched:
            # No matching token was found; add the current character as a token
            tokens.append(text[i])
            i += 1
    return tokens  # Return the list of tokens

# The transliteration function that converts input text into Bengali script
def transliterate(input_text):
    output = []  # Create an empty list to collect output characters
    tokens = tokenize(input_text)  # Break the input text into tokens using the tokenizer
    previous_was_consonant = False  # Flag to check if the last token was a consonant

    i = 0  # Initialize token index
    while i < len(tokens):  # Loop through each token
        token = tokens[i]  # Get the current token

        # If the token is a conjunct, add its Bengali mapping to output
        if token in conjuncts:
            output.append(conjuncts[token])  # Append the corresponding Bengali consonant
            previous_was_consonant = True  # Set flag to indicate last token was a consonant

        elif token in consonants:
            output.append(consonants[token])
            previous_was_consonant = True

        # If the token is a diacritic, add its Bengali mapping to output
        elif token in diacritics:
            output.append(diacritics[token])  # Append the corresponding Bengali consonant
            previous_was_consonant = False  # Set flag to indicate last token was a consonant

        # If the token is a reph, add its Bengali mapping to output
        elif token in reph:
            output.append(reph[token])  # Append the corresponding Bengali consonant
            previous_was_consonant = False  # Set flag to indicate last token was a consonant

        # If the token is a punctuation, add its Bengali mapping to output
        elif token in punctuations:
            output.append(punctuations[token])  # Append the corresponding Bengali consonant
            previous_was_consonant = False  # Set flag to indicate last token was a consonant

        # If the token matches r phola or z phola
        elif token in phola:
            if previous_was_consonant:
                output.append("্") # add hoshonto before appending r or z
                output.append(phola[token]) # then append r or z
            else:
                output.append(phola[token])
            previous_was_consonant = True  # Set flag to indicate last token was a consonant

        # If the token is a vowel
        elif token in vowels:
            # If it follows a consonant, use the diacritic (vowel sign)
            if previous_was_consonant:
                # Get the vowel sign if available, otherwise fall back to the full vowel
                output.append(vowel_signs.get(token, vowels[token]))
            else:
                # If not following a consonant, use the full vowel character
                output.append(vowels[token])
            previous_was_consonant = False  # Reset the consonant flag after processing a vowel

        elif token in vowel_signs:
            output.append(vowel_signs[token])
            previous_was_consonant = False
        elif token in digits:
            output.append(digits[token])
        # If the token is neither a consonant nor a vowel (like punctuation or space)
        else:
            output.append(token)  # Add the token unchanged
            previous_was_consonant = False  # Reset the flag

        i += 1  # Move to the next token

    return ''.join(output)  # Combine the list of characters into a string and return it

# Example usage: Continuous testing of the transliteration function
if __name__ == "__main__":
    # This block runs only when the script is executed directly, not when imported.
    print("Bengali IME Transliteration Tool")
    print("Type 'exit' to quit.")

    while True:
        # Prompt the user for input
        sample_input = input("Enter input: ")

        # If the user types "exit", break the loop and end the program
        if sample_input.lower() == "exit":
            break

        # Call the transliterate function with the provided input
        result = transliterate(sample_input)

        # Print the transliterated output
        print("Output:", result)
