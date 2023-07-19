import pandas as pd

import pandera as pa
from pandera.typing import Series, DateTime, Int, Float, String

class UserSchema(pa.DataFrameModel):
    # 各フィールドの定義と基本的なチェックを設定。
    id: Series[String] = pa.Field()  # idは文字列である
    age: Series[Float] = pa.Field(ge=18, le=60, coerce=True)  # 年齢は18以上60以下で、数値に強制変換する
    income: Series[pd.Int32Dtype] = pa.Field(ge=1, le=100000, coerce=True, nullable=True)  # 収入は1以上100000以下である
    gender: Series[String] = pa.Field(isin=["male", "female"])  # 性別は"male"か"female"
    job: Series[String] = pa.Field(nullable=True)  # 職業は文字列で、欠損値（None）も許容する
    hoge: Series[Int] = pa.Field(ge=1, le=10000000, coerce=True)  # hogeは1以上10000000以下で、数値に強制変換する
    datetime: Series[DateTime] = pa.Field(coerce=True)  # datetimeは日時である

    @pa.check("id")
    def id_split_check(cls, series: Series[str]) -> Series[bool]:
        """'_'でidを分割したときに2つの要素になることを確認する"""
        return series.str.split("_", expand=True).shape[1] == 2

    @pa.check("id")
    def id_length_check(cls, series: Series[str]) -> Series[bool]:
        """'_'でidを分割したときに、その2つの要素の文字数がそれぞれ2文字と4文字であることを確認する"""
        split_series = series.str.split("_", expand=True)
        return (split_series[0].str.len() == 2) & (split_series[1].str.len() == 4)
