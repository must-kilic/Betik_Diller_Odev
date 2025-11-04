from dosya_islemleri import read_csv, write_json,write_text
from processing import stats,build_report
def main():
    read_doc="/Users/musta/source/repos/betik_diller/exercise/data/people.csv"
    write_doc="/Users/musta/source/repos/betik_diller/exercise/data/stats.json"
    write_txt="/Users/musta/source/repos/betik_diller/exercise/datastats_txt.txt"

    rows = read_csv(read_doc)
    st = stats(rows)

    write_json(write_doc, st)
    write_text(write_txt, build_report(st))

    print("bitti")

if __name__=="__main__":
    main()