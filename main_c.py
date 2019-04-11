from c_langage.scanner import scan, ScanError
from parser import lr1
from c_langage.symbol import Terminal
from parser.tools import Item
import pickle
import sys


def main():
    try:
        fp = open('./data/c_parse_table.dat', 'rb')
    except FileNotFoundError:
        print(
            "Please run \"python %s make-parse-table\" before you first use this program." % sys.argv[0])
        return

    parse_tab, productions = pickle.load(fp)
    try:
        tokens, symbol_table, const_string_table = scan(sys.argv[1])
        res = lr1.prase(tokens, parse_tab, productions, Terminal, symbol_table, const_string_table,
                        simpify=True, show_tree_after_iteration=False)
        lr1.show_tree(res, symbol_table, const_string_table, max_symbol_len=13)
        print('符号表:')
        for s in symbol_table:
            print('\t',s)
        print('字符串表:')
        for s in const_string_table:
            print('\t"%s"'%s)
    except ScanError as e:
        e.show_error(sys.argv[1])
    except lr1.ParseError as e:
        e.show_error(sys.argv[1])

if __name__ == '__main__':
    main()
