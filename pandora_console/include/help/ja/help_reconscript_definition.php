<?php
/**
 * @package Include/help/ja
 */
?>
<h1>自動検出スクリプト定義</h1>

<p>"自動検出スクリプト" は、より柔軟に動作することができます。自動検出スクリプトは、ネットワークプラグインやエージェントプラグインのように、完全に特別なモニタ対象に対して個別対応できるように開発しました。それぞれの自動検出スクリプトは、それぞれの目的に応じて異なります。</p>

<p>基本的な考えは、システム内で検出したものを認識し、自動的に (ネットワーク、プラグイン、wmi などの) モニタリング対象にすることです。完全にカスタマイズ可能なため、Oracle データベースへの自動ログインをしたり、VirtualCenter で管理されている VMware 内に作られた新たな仮想ホストや、WebLogic アプリケーションサーバの新リクエストを検出したりできます。自動検出サーバを通して、好みのスケジュールで処理を実行することができます。</p>

<p>重要なフィールドは次の通りです。</p>

<p><b>スクリプトフルパス:</b> 実行スクリプトのパス</p>
