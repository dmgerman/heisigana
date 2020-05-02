#!/usr/bin/perl

while (<>) {
    chomp;
    @f = split('\t');
    print $f[0], "\t", "<a href='https://jisho.org/search/", $f[0], "%20%23kanji'>", $f[1], "</a>\n";
}
