from app import app, db, JudoTechnique, Kata

with app.app_context():
    db.drop_all()

    db.create_all()

    techniques = [
        # Te waza
        JudoTechnique(
            name="seoi-nage", belt="yellow", image_path="static/images/seoi-nage.png"
        ),
        JudoTechnique(
            name="ippon-seoi-nage",
            belt="yellow",
            image_path="static/images/ippon-seoi-nage.png",
        ),
        JudoTechnique(
            name="seoi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/seoi-otoshi.png",
        ),
        JudoTechnique(
            name="tai-otoshi",
            belt="UNKNOWN",
            image_path="static/images/tai-otoshi.png",
        ),
        JudoTechnique(
            name="kata-guruma",
            belt="UNKNOWN",
            image_path="static/images/kata-guruma.png",
        ),
        JudoTechnique(
            name="sukui-nage",
            belt="UNKNOWN",
            image_path="static/images/sukui-nage.png",
        ),
        JudoTechnique(
            name="obi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/obi-otoshi.png",
        ),
        JudoTechnique(
            name="uki-otoshi",
            belt="UNKNOWN",
            image_path="static/images/uki-otoshi.png",
        ),
        JudoTechnique(
            name="sumi-otoshi",
            belt="UNKNOWN",
            image_path="static/images/sumi-otoshi.png",
        ),
        JudoTechnique(
            name="yama-arashi",
            belt="UNKNOWN",
            image_path="static/images/yama-arashi.png",
        ),
        JudoTechnique(
            name="obi-tori-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/obi-tori-gaeshi.png",
        ),
        JudoTechnique(
            name="morote-gari",
            belt="UNKNOWN",
            image_path="static/images/morote-gari.png",
        ),
        JudoTechnique(
            name="kuchiki-taoshi",
            belt="UNKNOWN",
            image_path="static/images/kuchiki-taoshi.png",
        ),
        JudoTechnique(
            name="kibisu-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/kibisu-gaeshi.png",
        ),
        JudoTechnique(
            name="uchi-mata-sukashi",
            belt="UNKNOWN",
            image_path="static/images/uchi-mata-sukashi.png",
        ),
        JudoTechnique(
            name="ko-uchi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/ko-uchi-gaeshi.png",
        ),
        JudoTechnique(
            name="de-ashi-harai",
            belt="UNKNOWN",
            image_path="static/images/de-ashi-harai.png",
        ),
        JudoTechnique(
            name="okuri-ashi-harai",
            belt="UNKNOWN",
            image_path="static/images/okuri-ashi-harai.png",
        ),
        JudoTechnique(
            name="o-soto-otoshi",
            belt="yellow",
            image_path="static/images/o-soto-otoshi.png",
        ),
        JudoTechnique(
            name="hiza-guruma",
            belt="yellow",
            image_path="static/images/hiza-guruma.png",
        ),
        JudoTechnique(
            name="uchi-mata", belt="UNKNOWN", image_path="static/images/uchi-mata.png"
        ),
        JudoTechnique(
            name="tsurikomi-goshi",
            belt="UNKNOWN",
            image_path="static/images/tsurikomi-goshi.png",
        ),
        JudoTechnique(
            name="sasae-tsurikomi-ashi",
            belt="UNKNOWN",
            image_path="static/images/sasae-tsurikomi-ashi.png",
        ),
        JudoTechnique(
            name="ko-soto-gake",
            belt="UNKNOWN",
            image_path="static/images/ko-soto-gake.png",
        ),
        JudoTechnique(
            name="o-soto-gari",
            belt="yellow",
            image_path="static/images/o-soto-gari.png",
            youtube_id="c-A_nP7mKAc",
            description="Often first tachi waza technique you will learn",
        ),
        JudoTechnique(
            name="ashi-guruma",
            belt="UNKNOWN",
            image_path="static/images/ashi-guruma.png",
        ),
        JudoTechnique(
            name="o-uchi-gari",
            belt="yellow",
            image_path="static/images/o-uchi-gari.png",
        ),
        JudoTechnique(
            name="harai-tsurikomi-ashi",
            belt="UNKNOWN",
            image_path="static/images/harai-tsurikomi-ashi.png",
        ),
        JudoTechnique(
            name="ko-soto-gari",
            belt="yellow",
            image_path="static/images/ko-soto-gari.png",
        ),
        JudoTechnique(
            name="o-guruma", belt="UNKNOWN", image_path="static/images/o-guruma.png"
        ),
        JudoTechnique(
            name="ko-uchi-gari",
            belt="yellow",
            image_path="static/images/ko-uchi-gari.png",
        ),
        JudoTechnique(
            name="o-soto-guruma",
            belt="UNKNOWN",
            image_path="static/images/o-soto-guruma.png",
        ),
        JudoTechnique(
            name="o-uchi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/o-uchi-gaeshi.png",
        ),
        JudoTechnique(
            name="hane-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/hane-goshi-gaeshi.png",
        ),
        JudoTechnique(
            name="harai-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/harai-goshi-gaeshi.png",
        ),
        JudoTechnique(
            name="tsurikomi-goshi-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/tsurikomi-goshi-gaeshi.png",
        ),
        JudoTechnique(
            name="uchi-mata-gaeshi",
            belt="UNKNOWN",
            image_path="static/images/uchi-mata-gaeshi.png",
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
