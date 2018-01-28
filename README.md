# resovleWeb.py
目标爬取网站：http://ypk.familydoctor.com.cn/factory_11255_0_0_0_1_1.html
这个网站是 阿斯利康制药有限公司的药品大全，总共2页，共26个药品。

解析目标网站的单个li标签的结构
<li class="clearfix">

    <div class="pic">
        <a href="http://ypk.familydoctor.com.cn/63590/" target="_blank">
            <img alt="" height="125" src="http://ypk.familydoctor.com.cn/uploadFile/20150819/201508191546373892.jpg" width="160"/>
        </a>
        <p class="mj_db">＋加入对比</p>
    </div>


    <div class="text">
        <h3>
            <a href="http://ypk.familydoctor.com.cn/63590/" target="_blank">倍他乐克:酒石酸美托洛尔片</a>
        </h3>
    </div>
</li>

解析完成单个页面后，获取所有的商品的图片，文件url，并组成字典。
创建文件夹；
批量解析下载写入文件到本地。
