# python append.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/appendirr.csv
# python append.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/dropfirstlast.csv
# python append.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/dropfirst.csv
# python append.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/droplast.csv
# python append.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/shuffle.csv
python drop.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/droprandNN.csv
# python drop.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/droprandVB.csv
# python drop.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/dropallVB.csv
python drop.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/dropallNN.csv
python drop.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/dropallboth.csv
# python keep.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/keepVB.csv
python keep.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/keepNN.csv
python keep.py -i ../../data/Telugu/Data/iiit_hcu_inter_chunk_utf.ssf -o ../gold/telugu/keepboth.csv       