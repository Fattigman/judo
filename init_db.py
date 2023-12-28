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
            name="tai-otoshi",
            belt="orange",
            image_path="static/images/tai-otoshi.png",
        ),
        JudoTechnique(
            name="tani-otoshi",
            belt="green",
            image_path="static/images/tani-otoshi.png",
        ),
        JudoTechnique(
            name="kata-guruma",
            belt="brown",
            image_path="static/images/kata-guruma.png",
        ),
        JudoTechnique(
            name="sukui-nage",
            belt="brown",
            image_path="static/images/sukui-nage.png",
        ),
        JudoTechnique(
            name="uki-otoshi",
            belt="brown",
            image_path="static/images/uki-otoshi.png",
        ),
        JudoTechnique(
            name="uki-waza",
            belt="blue",
            image_path="static/images/uki-waza.png",
        ),
        JudoTechnique(
            name="uki-goshi",
            belt="orange",
            image_path="static/images/uki-otoshi.png",
        ),
        JudoTechnique(
            name="sumi-otoshi",
            belt="brown",
            image_path="static/images/sumi-otoshi.png",
        ),
        JudoTechnique(
            name="sumi-gaeshi",
            belt="blue",
            image_path="static/images/sumi-gaeshi.png",
        ),
        JudoTechnique(
            name="ushiro-goshi",
            belt="blue",
            image_path="static/images/ushiro-goshi.png",
        ),
        JudoTechnique(
            name="de-ashi-barai",
            belt="orange",
            image_path="static/images/de-ashi-barai.png",
        ),
        JudoTechnique(
            name="okuri-ashi-barai",
            belt="green",
            image_path="static/images/okuri-ashi-barai.png",
        ),
        JudoTechnique(
            name="o-soto-otoshi",
            belt="yellow",
            image_path="static/images/o-soto-otoshi.png",
        ),
        JudoTechnique(
            name="soto-makikomi",
            belt="blue",
            image_path="static/images/soto-makikomi.png",
        ),
        JudoTechnique(
            name="ura-nage",
            belt="blue",
            image_path="static/images/ura-nage.png",
        ),
        JudoTechnique(
            name="hiza-guruma",
            belt="yellow",
            image_path="static/images/hiza-guruma.png",
        ),
        JudoTechnique(
            name="uchi-mata", belt="orange", image_path="static/images/uchi-mata.png"
        ),
        JudoTechnique(
            name="tsuri-komi-goshi",
            belt="orange",
            image_path="static/images/tsuri-komi-goshi.png",
        ),
        JudoTechnique(
            name="tsuri-goshi",
            belt="orange",
            image_path="static/images/tsuri-goshi.png",
        ),
        JudoTechnique(
            name="sasae-tsuri-komi-ashi",
            belt="green",
            image_path="static/images/sasae-tsuri-komi-ashi.png",
        ),
        JudoTechnique(
            name="tomoe-nage",
            belt="green",
            image_path="static/images/tomoe-nage.png",
        ),
        JudoTechnique(
            name="ko-soto-gake",
            belt="orange",
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
            belt="blue",
            image_path="static/images/ashi-guruma.png",
        ),
        JudoTechnique(
            name="o-uchi-gari",
            belt="yellow",
            image_path="static/images/o-uchi-gari.png",
        ),
        JudoTechnique(
            name="harai-tsuri-komi-ashi",
            belt="green",
            image_path="static/images/harai-tsuri-komi-ashi.png",
        ),
        JudoTechnique(
            name="ko-soto-gari",
            belt="yellow",
            image_path="static/images/ko-soto-gari.png",
        ),
        JudoTechnique(
            name="o-guruma", belt="blue", image_path="static/images/o-guruma.png"
        ),
        JudoTechnique(
            name="ko-uchi-gari",
            belt="yellow",
            image_path="static/images/ko-uchi-gari.png",
        ),
        JudoTechnique(
            name="o-soto-guruma",
            belt="brown",
            image_path="static/images/o-soto-guruma.png",
        ),
        JudoTechnique(
            name="kami-shiho-gatame",
            belt="yellow",
            image_path="static/images/kami-shiho-gatame.png",
        ),
        JudoTechnique(
            name="mune-gatame",
            belt="yellow",
            image_path="static/images/mune-gatame.png",
        ),
        JudoTechnique(
            name="kuzure-kesa-gatame",
            belt="yellow",
            image_path="static/images/kuzure-kesa-gatame.png",
        ),
        JudoTechnique(
            name="juji-gatame",
            belt="orange",
            image_path="static/images/juji-gatame.png",
        ),
        JudoTechnique(
            name="hane-goshi",
            belt="blue",
            image_path="static/images/hane-goshi.png",
        ),
        JudoTechnique(
            name="harai-goshi",
            belt="orange",
            image_path="static/images/harai-goshi.png",
        ),
        JudoTechnique(
            name="yoko-otoshi",
            belt="blue",
            image_path="static/images/yoko-otoshi.png",
        ),
        JudoTechnique(
            name="yoko-gake",
            belt="blue",
            image_path="static/images/yoko-gake.png",
        ),
        JudoTechnique(
            name="yoko-guruma",
            belt="blue",
            image_path="static/images/yoko-guruma.png",
        ),
        JudoTechnique(
            name="utsuri-goshi",
            belt="brown",
            image_path="static/images/utsuri-goshi.png",
        ),
        JudoTechnique(
            name="yoko-wakare",
            belt="brown",
            image_path="static/images/yoko-wakare.png",
        ),
        JudoTechnique(
            name="hane-maki-komi",
            belt="brown",
            image_path="static/images/hane-maki-komi.png",
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
