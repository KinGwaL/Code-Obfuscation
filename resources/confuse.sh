#!/usr/bin/env bash

TABLENAME=symbols
SYMBOL_DB_FILE="$PROJECT_DIR/$PROJECT_NAME/Resource/symbols"
STRING_SYMBOL_FILE="$PROJECT_DIR/$PROJECT_NAME/Resource/func.list"
PRESTRING_SYMBOL_FILE="$PROJECT_DIR/$PROJECT_NAME/Resource/prefunc.list"
CONFUSE_FILE="$PROJECT_DIR/"

HEAD_FILE="$PROJECT_DIR/$PROJECT_NAME/Resource/codeObfuscation.h"

export LC_CTYPE=C

#取以.m或.h結尾的文件以+號或-號開頭的行|去掉所有+號或－號|用空格代替符號|n個空格跟著<號替換成<號|開頭不能是IBAction|用空格split字串取第二部分|排序|去重複|刪除空行|刪掉以init開頭的行>寫進prefunc.list
#由於不能排掉所有非系統功能，所以只能放入prefunc.list 再由人手搬至 func.list
grep -h -r -I  "^[-+]" $CONFUSE_FILE  --include '*.[mh]' |sed "s/[+-]//g"|sed "s/[();,: *\^\/\{]/ /g"|sed "s/[ ]*</</"| sed "/^[ ]*IBAction/d"|awk '{split($0,b," "); print b[2]; }'| sort|uniq |sed "/^$/d"|sed -n "/^/p" >$PRESTRING_SYMBOL_FILE


#維護數據庫方便日後作排重
createTable()
{
echo "create table $TABLENAME(src text, des text);" | sqlite3 $SYMBOL_DB_FILE
}

insertValue()
{
echo "insert into $TABLENAME values('$1' ,'$2');" | sqlite3 $SYMBOL_DB_FILE
}

query()
{
echo "select * from $TABLENAME where src='$1';" | sqlite3 $SYMBOL_DB_FILE
}

ramdomString()
{
openssl rand -base64 64 | tr -cd 'a-zA-Z' |head -c 16

}

rm -f $SYMBOL_DB_FILE
rm -f $HEAD_FILE
createTable

touch $HEAD_FILE
echo '#ifndef Demo_codeObfuscation_h
#define Demo_codeObfuscation_h' >> $HEAD_FILE
echo "//confuse string at `date`" >> $HEAD_FILE
cat "$STRING_SYMBOL_FILE" | while read -ra line; do
if [[ ! -z "$line" ]]; then
ramdom=`ramdomString`
echo $line $ramdom
insertValue $line $ramdom
echo "#define $line $ramdom" >> $HEAD_FILE
fi
done
echo "#endif" >> $HEAD_FILE


sqlite3 $SYMBOL_DB_FILE .dump

