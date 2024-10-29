from pelican import signals

@signals.article_generator_finalized.connect
def add_seasons_to_context(generator):

    articles = generator.articles

    # 重複のないシーズンを収集するためにセットを使用
    unique_seasons = sorted(
        {article.metadata.get('season') for article in articles if article.metadata.get('season')},
        reverse=True
    )
    #変数をグローバル領域にセット
    generator.context['seasons'] = unique_seasons

    # ユニークなシーズンとシーズンごとの記事を収集
    season_articles = {}
    y = []
    for target in unique_seasons:
        season_articles = [article for article in articles if article.metadata.get('season') == target]

        period = {
            'dates': season_articles,
            'articles': season_articles,
            'save_as': f"season/{target}.html",
            'url': f"season/{target}.html",
            'period': (target,),
            'period_num': (target,)
        }
        y.append(period)

    # period_archivesにアーカイブス(年や月単位のarticlesを保持)があるのでそこを任意のデータセットに差し替える
    # もしかしたらpelicanconf.pyにYEAR_ARCHIVE_SAVE_AS定義していないと正しく動かないかも？
    generator.period_archives['year'] = y
