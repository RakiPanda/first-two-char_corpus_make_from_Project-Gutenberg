データソース：https://www.gutenberg.org/ebooks/84, https://www.gutenberg.org/ebooks/1342

手順<br>
１．corpus_make_from_ProjectGutenberg_no_final_chapter_forXXX.pyを実行し，最後のchapterを除いた学習用コーパスを作成する．<br>
２．test_data_make_from_ProjectGutenberg_only_final_chapter_forXXX.pyを実行し，最後のchapterのみからなるテスト用データを作成する．<br>
３．生成されたfirst-two-char_corpus_fromXXX_no_final_chapter.txtとtest_data_only_final_chapter_XXX.txtをKyTeaのファイルの中に入れる．<br>
４．KyTeaで以下のようにコマンドを実施し，学習とテストをする．<br>
    ```
        suzuki@DESKTOP-XXX:~/kytea-0.4.7$ train-kytea -full first-two-char_corpus_from84_no_final_chapter.txt -model first-two-char_corpus_from84_no_final_chapter.mod
        Scanning dictionaries and corpora for vocabulary
        Reading corpus from first-two-char_corpus_from84_no_final_chapter.txt  done (2732 lines)
        Building dictionary index done!
        Creating word segmentation features .. done!
        Building classifier  done!
        Creating tagging features (tag 1) done!
        Training local tag classifiers done!
        Printing model to first-two-char_corpus_from84_no_final_chapter.mod done!
        suzuki@DESKTOP-XXX:~/kytea-0.4.7$ kytea -model first-two-char_corpus_from84_no_final_chapter.mod < test_data_only_final
        _chapter_1342-0.txt > result_test_data_only_final_chapter_1342-0.txt
    ```<br>
５．KyTeaで生成されたresult_test_data_only_final_chapter_XXX.txtをREADME.mdが入っているファイルにコピーする．<br>
６．delete_UNK_form_result_XXX.pyを実行する．<br>
７．estimated_sentence_from_result_test_data_XXX.pyを実行する．<br>
８．processing_final_chapter_origin_for_comparison_XXX.pyを実行する．<br>
９．calculate_accuracy_XXX.pyを実行する．<br>
１０．XXX_accuracy.csvファイルが生成されているので，完成．<br>