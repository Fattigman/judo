from app import app, db, JudoTechnique, Kata

with app.app_context():
    db.drop_all()

    db.create_all()

    techniques = [
        # Te waza
        JudoTechnique(
            name="seoi-nage", belt="yellow", image_path="static/images/seoi_nage.jpeg"
        ),
        JudoTechnique(
            name="ippon-seoi-nage",
            belt="yellow",
            image_path="static/images/ippon_seoi_nage.jpeg",
        ),
        JudoTechnique(
            name="seoi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/seoi_otoshi.jpeg",
        ),
        JudoTechnique(
            name="tai-otoshi",
            belt="UNKNOWN",
            image_path="static/images/tai_otoshi.jpeg",
        ),
        JudoTechnique(
            name="kata-guruma",
            belt="UNKNOWN",
            image_path="static/images/kata_guruma.jpeg",
        ),
        JudoTechnique(
            name="sukui-nage",
            belt="UNKNOWN",
            image_path="static/images/sukui_nage.jpeg",
        ),
        JudoTechnique(
            name="obi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/obi_otoshi.jpeg",
        ),
        JudoTechnique(
            name="uki-otoshi",
            belt="UNKNOWN",
            image_path="static/images/uki_otoshi.jpeg",
        ),
        JudoTechnique(
            name="sumi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/sumi_otoshi.jpeg",
        ),
        JudoTechnique(
            name="yama-arashi",
            belt="UNKNOWN",
            image_path="static/images/yama_arashi.jpeg",
        ),
        JudoTechnique(
            name="obi-tori-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/obi_tori_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="morote-gari",
            belt="UNKNOWN",
            image_path="static/images/morote_gari.jpeg",
        ),
        JudoTechnique(
            name="kuchiki-taoshi",
            belt="UNKNOWN",
            image_path="static/images/kuchiki_taoshi.jpeg",
        ),
        JudoTechnique(
            name="kibisu-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/kibisu_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="uchi-mata-sukashi",
            belt="UNKNOWN",
            image_path="static/images/uchi_mata_sukashi.jpeg",
        ),
        JudoTechnique(
            name="ko-uchi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/ko_uchi_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="de-ashi-harai",
            belt="UNKNOWN",
            image_path="static/images/de_ashi_harai.jpeg",
        ),
        JudoTechnique(
            name="okuri-ashi-harai",
            belt="UNKNOWN",
            image_path="static/images/okuri_ashi_harai.jpeg",
        ),
        JudoTechnique(
            name="o-soto-otoshi",
            belt="yellow",
            image_path="static/images/o_soto_otoshi.jpeg",
        ),
        JudoTechnique(
            name="hiza-guruma",
            belt="yellow",
            image_path="static/images/hiza_guruma.jpeg",
        ),
        JudoTechnique(
            name="uchi-mata", belt="UNKNOWN", image_path="static/images/uchi_mata.jpeg"
        ),
        JudoTechnique(
            name="tsurikomi-goshi",
            belt="UNKNOWN",
            image_path="static/images/tsurikomi_goshi.jpeg",
        ),
        JudoTechnique(
            name="sasae-tsurikomi-ashi",
            belt="UNKNOWN",
            image_path="static/images/sasae_tsurikomi_ashi.jpeg",
        ),
        JudoTechnique(
            name="ko-soto-gake",
            belt="UNKNOWN",
            image_path="static/images/ko_soto_gake.jpeg",
        ),
        JudoTechnique(
            name="o-soto-gari",
            belt="yellow",
            image_path="static/images/o_soto_gari.jpeg",
            youtube_id="c-A_nP7mKAc",
            description="Often first tachi waza technique you will learn",
        ),
        JudoTechnique(
            name="ashi-guruma",
            belt="UNKNOWN",
            image_path="static/images/ashi_guruma.jpeg",
        ),
        JudoTechnique(
            name="o-uchi-gari",
            belt="yellow",
            image_path="static/images/o_uchi_gari.jpeg",
        ),
        JudoTechnique(
            name="harai-tsurikomi-ashi",
            belt="UNKNOWN",
            image_path="static/images/harai_tsurikomi_ashi.jpeg",
        ),
        JudoTechnique(
            name="ko-soto-gari",
            belt="yellow",
            image_path="static/images/ko_soto_gari.jpeg",
        ),
        JudoTechnique(
            name="o-guruma", belt="UNKNOWN", image_path="static/images/o_guruma.jpeg"
        ),
        JudoTechnique(
            name="ko-uchi-gari",
            belt="yellow",
            image_path="static/images/ko_uchi_gari.jpeg",
        ),
        JudoTechnique(
            name="o-soto-guruma",
            belt="UNKNOWN",
            image_path="static/images/o_soto_guruma.jpeg",
        ),
        JudoTechnique(
            name="o-uchi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/o_uchi_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="hane-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/hane_goshi_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="harai-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/harai_goshi_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="tsurikomi-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/tsurikomi_goshi_gaeshi.jpeg",
        ),
        JudoTechnique(
            name="uchi-mata-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/uchi_mata_gaeshi.jpeg",
        ),
    ]

    katas = [
        Kata(name="Nage no Kata"),
        Kata(name="Katame no Kata"),
        Kata(name="Kime no Kata"),
        Kata(name="Kodokan Goshin Jutsu"),
        Kata(name="Ju no Kata"),
        Kata(name="Itsuku no Kata"),
        Kata(name="Koshiki no Kata"),
        Kata(name="Seiryoku Zen´yo Kokumin Taiiku"),
    ]

    for technique in techniques:
        db.session.add(technique)
        db.session.commit()

    for kata in katas:
        db.session.add(kata)
        db.session.commit()
