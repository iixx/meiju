#coding:utf-8
import re

html = """
<iframe frameborder="0" style="display: none;"></iframe><div id="bdshare_s" style="display: block;"><iframe id="bdsIfr" style="position:absolute;display:none;z-index:9999;" frameborder="0"></iframe><div id="bdshare_l" style="display: none;"><div id="bdshare_l_c"><h6>分享到</h6><ul><li><a href="#" class="bds_mshare mshare">一键分享</a></li><li><a href="#" class="bds_qzone qqkj">QQ空间</a></li><li><a href="#" class="bds_tsina xlwb">新浪微博</a></li><li><a href="#" class="bds_bdysc bdysc">百度云收藏</a></li><li><a href="#" class="bds_renren rrw">人人网</a></li><li><a href="#" class="bds_tqq txwb">腾讯微博</a></li><li><a href="#" class="bds_bdxc bdxc">百度相册</a></li><li><a href="#" class="bds_kaixin001 kxw">开心网</a></li><li><a href="#" class="bds_tqf txpy">腾讯朋友</a></li><li><a href="#" class="bds_tieba bdtb">百度贴吧</a></li><li><a href="#" class="bds_douban db">豆瓣网</a></li><li><a href="#" class="bds_tsohu shwb">搜狐微博</a></li><li><a href="#" class="bds_bdhome bdhome">百度新首页</a></li><li><a href="#" class="bds_sqq sqq">QQ好友</a></li><li><a href="#" class="bds_thx thx">和讯微博</a></li><li><a href="#" class="bds_more">更多...</a></li></ul><p><a href="#" class="goWebsite">百度分享</a></p></div></div></div><div id="wrapper">

  <div id="header">
     <div class="headertop">
       <img src="http://www.ttmeiju.com/templates/ttmeiju/images/logo.gif" alt="天天美剧" class="logo">
      
       <div id="user_login">
<script src="http://www.ttmeiju.com/batch.panel.php?open=1&amp;rand=168763" type="text/javascript" language="javascript"></script><div class="fixedheight"><div id="user_login_position"><div id="login_authcode_img" style="display:none"><img src="http://www.ttmeiju.com/do.php?action=seccode" alt="验证码" id="img_seccode"></div><form id="login_box" action="http://www.ttmeiju.com/batch.login.php?action=login" method="post"><input type="hidden" name="formhash" value="92c4eded"><label>用户名:</label> <input type="text" name="username" class="input_tx" size="23" onfocus="addseccode();" tabindex="1">&nbsp;&nbsp;&nbsp;<label>密&nbsp;&nbsp;&nbsp;码:</label> <input type="password" name="password" class="input_tx" size="23" onfocus="addseccode();" tabindex="2"><p id="login_authcode_input" style="display:none"><label>验证码:</label> <input type="text" class="input_tx" name="seccode" size="10" onfocus="showseccode()" ;="" tabindex="3"> <a href="javascript:updateseccode();">换一张</a></p>&nbsp;&nbsp;<input id="cookietime" type="checkbox" value="315360000" name="cookietime" class="input_remember" tabindex="4"><label class="label_remember" for="cookietime">记住我</label><input type="submit" name="loginsubmit" class="input_sub" value="登录" tabindex="5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://bbs.ttmeiju.com/member.php?mod=register">注册新用户</a> |&nbsp;&nbsp;&nbsp;<a href="http://bbs.ttmeiju.com/member.php?mod=logging&amp;action=login&amp;viewlostpw=1">找回密码</a><font color="red">&nbsp;&nbsp;(您可以使用论坛账户登陆)</font></form></div></div>
       </div>  
     </div>

      <ul class="menu">
         <li style="width:80px;">&nbsp;</li>
         <a href="http://www.ttmeiju.com/"><li>首页</li></a>
         <a href="http://www.ttmeiju.com/usershare.html"><li>众乐乐</li></a>
         <a href="http://www.ttmeiju.com/weekcalendar.html"><li>时间表</li></a>
         <a href="http://www.ttmeiju.com/countdown.html"><li>回归倒计时</li></a>
         <a href="http://www.ttmeiju.com/summary.html"><li>美剧排行榜</li></a>
         <a href="http://bbs.ttmeiju.com" target="_blank"><li>论坛</li></a>
         <a href="http://weibo.com/ttmeiju" rel="nofollow" target="_blank"><li>微博</li></a>
         <a href="http://bbs.ttmeiju.com/forum.php?mod=forumdisplay&amp;fid=38"><li>站长留言</li></a>
      </ul>
    
      
 <ul class="headad">
        <li><a href="http://s.click.taobao.com/FAbCf4y" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/DqkX81y" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/SpkLT5y" target="_blank"></a></li>
     </ul>
    
    
      
 <ul class="headad">
        <li><a href="http://s.click.taobao.com/P7EjUBy" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/t?e=m%3D2%26s%3DjFNk4cJaeiwcQipKwQzePDAVflQIoZepK…dwB0jwE0VqMMgx22UI05YlSlxDMrvDCYy6CIAzXVuTsfw2smna1oh7E2SHQsrL7jmrsalu6Lyn" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/ADwfj4y" target="_blank"></a></li>
     </ul>
    
    
      
 <ul class="headad">
        <li><a href="http://s.click.taobao.com/Jbf09yx" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/zZoQ81y" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/kC5yKCy" target="_blank"></a></li>
     </ul>
    
    
      
 <ul class="headad">
        <li><a href="http://s.click.taobao.com/wHTRyxx" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/FAbCf4y" target="_blank"></a></li>
        <li><a href="http://s.click.taobao.com/yswpKCy" target="_blank"></a></li>
     </ul>
    
  </div><div id="midder">
    <div class="content">
        <div class="newscontent contentbox">
            <div class="hd"><h3>基本演绎法 Elementary-基本演绎法下载-基本演绎法全集下载-Elementary下载</h3></div>
            <div class="bd">
                <div class="clear" style="text-align:center;">
                    
                    <div class="seedpic"></div>
<script type="text/javascript">
var spic = document.getElementById("spic");
var ua = navigator.userAgent.toLowerCase();   
//alert(ua);   
if (ua.indexOf("webkit") > -1) {spic.width=500;}
else {
    var img = new Image();
    img.src = "http://pic.yupoo.com/ttmeiju/EaHmyYy8/medish.jpg";
   // alert(img.width + ":" + img.height); 
    if(img.width>img.height) {spic.width=500;}
    else {spic.height=500;}

}
</script>
                    
                    <div class="seedlink">
                        
                        <table class="seedtable" border="0" align="center" cellpadding="1" cellspacing="1" bgcolor="#cccccc" width="100%">
                          <tbody><tr align="center">
                            <td bgcolor="#fafafa" width="20%" align="right">更新日：</td>
                            
                            
                                                        <td bgcolor="#ffffff" width="80%" align="left">每周五</td>
                            
                          </tr>
                          <tr align="center">
                            <td bgcolor="#fafafa" align="right">状态：</td>
                                                        <td bgcolor="#ffffff" align="left"><font color="red">本季终</font></td>
                          </tr>
                          <tr align="center">
                            <td bgcolor="#fafafa" align="right">发布时间：</td>
                            <td bgcolor="#ffffff" align="left">2012-09-06 10:38</td>
                          </tr>
                          <tr align="center">
                            <td bgcolor="#fafafa" align="right">最后更新：</td>
                            <td bgcolor="#ffffff" align="left">2015-06-10 10:34</td>
                          </tr>
                          <tr align="center">
                            <td bgcolor="#fafafa" align="right">回归：</td>
                            <td bgcolor="#ffffff" align="left">
2015-11-06</td>
                          </tr>
                          
                          <tr align="center">
                            <td bgcolor="#fafafa" align="right">倒计时：</td>
                            <td bgcolor="#ffffff" align="left">
82天
</td>
                          </tr>
                          
                          <tr align="center">
                            <td bgcolor="#ffffff" align="center" colspan="2"><a href="javascript:void()" onclick="RSS_PRO('add',408);showRSSPROmsg($(this),2,408)">关注本剧，以便获得最新剧集</a> / 已有[ 1742 ] 人关注</td>
                          </tr>
                          
                          <tr><td colspan="2" bgcolor="#FFFFFF" height="35">
                              <!-- Baidu Button BEGIN -->
                              <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
                              <span class="bds_more">分享到：</span>
                              <a class="bds_qzone" title="分享到QQ空间" href="#"></a>
                              <a class="bds_tsina" title="分享到新浪微博" href="#"></a>
                              <a class="bds_tqq" title="分享到腾讯微博" href="#"></a>
                              <a class="bds_renren" title="分享到人人网" href="#"></a>
                              <a class="bds_t163" title="分享到网易微博" href="#"></a>
                              <a class="shareCount" href="#" title="累计分享0次">0</a>
                              </div>
                              <script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=6609072" src="http://bdimg.share.baidu.com/static/js/bds_s_v2.js?cdnversion=399922"></script>
                              
                              <script type="text/javascript">
                              document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000);
                              </script>
                              <!-- Baidu Button END -->
                          </td></tr>                          
                        </tbody></table>
                    </div>
                    
                    
                </div> 
                <div class="newstxt" style="min-height:inherit;">
                   <div>	该剧是「美国版」的现代福尔摩斯故事，英国BBC曾一度威胁要状告该剧剽窃英国版《新编福尔摩斯》（Sherlock）的创意，虽然最终不了了之，但CBS为避免惹官司确实下了一番苦心??他们把经典人物「华生」改成了一位女性！而且是亚裔女性！ Jonny Lee Miller在该剧中扮演主人公夏洛克?福尔摩斯（Sherlock Holmes），刘玉玲（Lucy Liu）扮演福尔摩斯的挚友兼搭档琼?华生（Joan Watson）。他们是纽约市警署聘请的特别顾问，正因为这个「特别」，他们接手的都是其他人毫无头绪的悬案。</div><div>	在本剧中，福尔摩斯曾经是苏格兰场（伦敦**厅）的著名侦探，大名响彻英伦三岛，却因为酗酒（或者吸毒，或者像豪斯医生一样服药上瘾，新闻稿没有说清楚）的问题让自己蒙羞，被送入相关机构强制戒酒。机智的福尔摩斯逃离了这家机构，渡过大西洋辗转来到美国的曼哈顿。他有钱的父亲决定给他点教训??让他和另一位正在努力戒酒的瘾君子共同生活。那对福尔摩斯来说无异是一场恶梦，因为……这位瘾君子??华生医生??是个女人！华生曾是事业有成的外科医生，却因为酒瘾害死一名病人，三年前失去了医师执照。福尔摩斯的父亲雇佣华生担任福尔摩斯的「私人康复助理」，华生将这份工作当做帮助别人并给自己赎罪的机会。糟糕的是，福尔摩斯和华生以前的客户完全不同，他永远都不安分！福尔摩斯直截了当地告诉华生，她的那套「康复技能」对他来说根本不管用。他已经发明了自己的「戒酒养生法」??给纽约市警署当特别顾问，用破案来填充自己空虚的日常生活。华生无可奈何，只有奉陪到底。福尔摩斯很快发现华生并非一无是处，相反，她的医学特长对他帮助很大。而华生也意识到，她天生就是当侦探的材料。</div><div>	纽约市警署的Tobias “Toby” Gregson警长（Aidan Quinn）是福尔摩斯的朋友，911事件之后曾与福尔摩斯一起工作过一段时间，对他破案的能力印象深刻。当他听说福尔摩斯来到美国之后，立即张开双臂欢迎他加入自己的团队。Gregson知道福尔摩斯在英国经常使用「反常手段」来办案，那些手段在美国根本行不通。而且福尔摩斯个性桀骜不驯，如果不加约束肯定会惹出大麻烦。Gregson迫切需要一个人能时时刻刻盯着福尔摩斯??本质上来说，这项工作就是为华生准备的。 剧组在动漫大会、TCA见面会等多种场合下反复强调：福尔摩斯与华生之间不会产生爱情关系，害怕该剧「胡搞」经典故事的观众可以放一百个心。</div>                </div>
                <div class="seedlistdiv">
                    
                <table class="seedtable" cellpadding="1" cellspacing="1">
                  <tbody><tr class="Stitle">
                    <td height="28" colspan="7" align="left"><h3>基本演绎法 Elementary 的所有种子</h3></td>
                  </tr>
                  <tr class="Shead">
                    <td width="5%" align="center">序号</td>
                    <td width="45%" align="left">名字</td>
                    
<td width="15%">Download</td>
                    <td width="6%">Size</td>
                    <td width="5%">格式</td>
                    <td width="10%">字幕下载</td>
                    <td width="5%">讨论</td>
                  </tr><!--seed_list-->      
 
      <tr class="Scontent">
                    <td>1</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/41132.html">
基本演绎法 Elementary S03E24 480p 伊甸园字幕组 季终</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s41132" onclick="SHOWSECCODE(41132)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?UNreyyQ" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>2</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/41072.html">
基本演绎法 Elementary S03E23 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s41072" onclick="SHOWSECCODE(41072)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?UNreyyQ" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>3</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40894.html">
基本演绎法 Elementary S03E22 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s40894" onclick="SHOWSECCODE(40894)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?faAVFjv" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>4</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40741.html">
基本演绎法 Elementary S03E21 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s40741" onclick="SHOWSECCODE(40741)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?YvIvIbI" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>5</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40392.html">
基本演绎法 Elementary S03E24 1080p WEB-DL</a></td>
                    
                    <td>
                     <!--if 1.55}>
                          <span id="s40392" onclick="SHOWSECCODE(40392)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1c0fJy5y" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:f3c675bee65d33a03e5d65e771b7c88197df2be6&amp;dn=Elementary.S03E24.1080p.WEB-DL.DD5.1.H.264-Juggalotus%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarb" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>1.55 G</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>6</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40386.html">
基本演绎法 Elementary S03E20 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s40386" onclick="SHOWSECCODE(40386)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?VvuyQjj" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>7</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40336.html">
基本演绎法 Elementary S03E24 720p</a></td>
                    
                    <td>
                     <!--if 840}>
                          <span id="s40336" onclick="SHOWSECCODE(40336)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1jGrIzJo" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:eca537a0c7213ae7c574019b91c51032ec2dd00c&amp;dn=Elementary.S03E24.720p.HDTV.X264-DIMENSION%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>840 M</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>8</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40335.html">
基本演绎法 Elementary S03E24</a></td>
                    
                    <td>
                     <!--if 216}>
                          <span id="s40335" onclick="SHOWSECCODE(40335)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1hqmwK1A" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:d5ad44b4f5001acf42814736f2aa601d8ce93d07&amp;dn=Elementary.S03E24.HDTV.x264-LOL%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>216 M</td>
                    <td>mp4</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>9</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/40040.html">
基本演绎法 Elementary S03E23 1080p WEB-DL</a></td>
                    
                    <td>
                     <!--if 1.59}>
                          <span id="s40040" onclick="SHOWSECCODE(40040)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1i3F0MY5" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:b5deceb5f43fd1201c78d24d611fee7b7d8463f0&amp;dn=Elementary.S03E23.Absconded.1080p.WEB-DL.DD5.1.H.264-Juggalotus%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>1.59 G</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>10</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39944.html">
基本演绎法 Elementary S03E19 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s39944" onclick="SHOWSECCODE(39944)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?F7VVVzi" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>11</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39910.html">
基本演绎法 Elementary S03E23 720p</a></td>
                    
                    <td>
                     <!--if 867}>
                          <span id="s39910" onclick="SHOWSECCODE(39910)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1pq50y" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:a1a24a130c15416615f7cb86bc99de07067177d6&amp;dn=Elementary.S03E23.720p.HDTV.X264-DIMENSION%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>867 M</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>12</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39909.html">
基本演绎法 Elementary S03E23</a></td>
                    
                    <td>
                     <!--if 215}>
                          <span id="s39909" onclick="SHOWSECCODE(39909)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1qW2viRM" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:1fa978980f24a511281ed9e758484b46a4363fee&amp;dn=Elementary.S03E23.HDTV.x264-LOL%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710&amp;tr=udp" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>215 M</td>
                    <td>mp4</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>13</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39776.html">
基本演绎法 Elementary S03E18 480p 伊甸园字幕组</a></td>
                    
                    <td>
                     <!--if 280}>
                          <span id="s39776" onclick="SHOWSECCODE(39776)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bniyCph" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                       <a href="http://urlxf.qq.com/?Jzaiy2m" rel="nofollow" target="_blank" title="旋风mkv美剧"><img src="/templates/ttmeiju/images/d5.gif" alt="旋风mkv美剧"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="http://bbs.sfile2012.com/viewthread.php?tid=383942" rel="nofollow" target="_blank" title="其他"><img src="/templates/ttmeiju/images/d2.gif" alt="其他"></a>
                     
                    </td>
                    
                    <td>280 M</td>
                    <td>mp4</td>
                    <td>
                    
     
            <font color="#339999">内嵌中文字幕</font>
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>14</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39552.html">
基本演绎法 Elementary S03E22 1080p WEB-DL</a></td>
                    
                    <td>
                     <!--if 1.55}>
                          <span id="s39552" onclick="SHOWSECCODE(39552)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1eQq3YyY" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:3a7cdc0a5e1d438a6c3cfd1ab375db389192fce4&amp;dn=Elementary.S03E22.The.Best.Way.Out.is.Always.Through.1080p.WEB-DL.DD5.1.H.264-Juggalotus%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg." rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>1.55 G</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>15</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39516.html">
基本演绎法 Elementary S03E22 720p</a></td>
                    
                    <td>
                     <!--if 715}>
                          <span id="s39516" onclick="SHOWSECCODE(39516)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1wbNWy" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:0d97ef07f00ec819e9d4baed9c3c5b875a23aad1&amp;dn=Elementary.S03E22.720p.HDTV.X264-DIMENSION%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>715 M</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>16</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39515.html">
基本演绎法 Elementary S03E22</a></td>
                    
                    <td>
                     <!--if 183}>
                          <span id="s39515" onclick="SHOWSECCODE(39515)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1jGCG3J4" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:c7d36c1be21d741b150ed9a394195ce4c2393766&amp;dn=Elementary.S03E22.HDTV.x264-LOL%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710&amp;tr=udp" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>183 M</td>
                    <td>mp4</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>17</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39196.html">
基本演绎法 Elementary S03E21 1080p WEB-DL</a></td>
                    
                    <td>
                     <!--if 1.56}>
                          <span id="s39196" onclick="SHOWSECCODE(39196)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1pJLZ3T5" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:e019f06d78912d4c09b27d9fe87001a4527b4302&amp;dn=Elementary.S03E21.Under.My.Skin.1080p.WEB-DL.DD5.1.H.264-Juggalotus%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>1.56 G</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>18</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39116.html">
基本演绎法 Elementary S03E21 720p</a></td>
                    
                    <td>
                     <!--if 766}>
                          <span id="s39116" onclick="SHOWSECCODE(39116)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1o6OJpqy" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:ca5431508c2a0357a58c07640d394dfd6a84fa54&amp;dn=Elementary.S03E21.720p.HDTV.X264-DIMENSION%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>766 M</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>19</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/39115.html">
基本演绎法 Elementary S03E21</a></td>
                    
                    <td>
                     <!--if 189}>
                          <span id="s39115" onclick="SHOWSECCODE(39115)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1bn0di5T" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:ae2cfe0256ef3651136d0dd5769d421649d67e78&amp;dn=Elementary.S03E21.HDTV.x264-LOL%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710&amp;tr=udp" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>189 M</td>
                    <td>mp4</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
      <tr class="Scontent">
                    <td>20</td>                    
                    <td align="left"><a href="http://www.ttmeiju.com/seed/38739.html">
基本演绎法 Elementary S03E20 1080p WEB-DL</a></td>
                    
                    <td>
                     <!--if 1.55}>
                          <span id="s38739" onclick="SHOWSECCODE(38739)" style="cursor:pointer">点击获取下载地址</span>
                     <!--/if}-->
                     
                       <a href="http://pan.baidu.com/s/1dDtTlqp" rel="nofollow" target="_blank" title="百度云盘下载"><img src="/templates/ttmeiju/images/d7.gif" alt="百度云盘"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                       <a href="magnet:?xt=urn:btih:eeb845e76518f78444aaea95c95633167eadd829&amp;dn=Elementary.S03E20.A.Stitch.in.Time.1080p.WEB-DL.DD5.1.H.264-Juggalotus%5Brartv%5D&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2710&amp;tr=u" rel="nofollow" target="_blank" title="磁力链高清美剧下载"><img src="/templates/ttmeiju/images/d3.gif" alt="磁力链高清美剧下载"></a>
                     
                     
                     
                     
                     
                     
                     
                     
                     
                    </td>
                    
                    <td>1.55 G</td>
                    <td>mkv</td>
                    <td>
                    
     
         
 

         
                <a href="http://www.addic7ed.com/overview/30750/Elementary" target="_blank" rel="nofollow">搜英</a>
         
         
         
     
                    </td>
                    <td>
               
                  </td></tr> 
     
 
                 <tr bgcolor="#ffffff"><td colspan="7" height="30" style="padding-top:8px;"><div class="pages"><div><strong>1</strong><a href="?page=2">2</a><a href="?page=3">3</a><a href="?page=4">4</a><a href="?page=5">5</a><a href="?page=6">6</a><a href="?page=7">7</a><a href="?page=8">8</a><a href="?page=9">9</a><a href="?page=10">10</a><a class="next" href="?page=2">下一页</a></div></div></td></tr> 
                </tbody></table>
                
                </div>
            </div>
        </div>
    </div>
  </div>
<div id="footer">
  
        <script src="http://vpie.net/cx30_2.js"></script> <div id="footer_top">
<p class="good_link">
<a href="http://www.ttmeiju.com/index.php">天天美剧</a>　|　
            <a href="/about-3.html">联系我们</a>　|　
            <a href="http://www.jnoy120.cn" target="_blank" style="display:none">济南泌尿医院</a>
</p>
 </div>
 <div class="copyright">
<p id="copyright">
   Powered by ttmeiju.com <em title="20091126">7.5</em> © 2011-2014　ttmeiju.com <br> ReDevelop &amp; Design By DeadLich
          <script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F52542b48446553babc42e4baae658e27' type='text/javascript'%3E%3C/script%3E"));
</script><script src=" http://hm.baidu.com/h.js?52542b48446553babc42e4baae658e27" type="text/javascript"></script><a href="http://tongji.baidu.com/hm-web/welcome/ico?s=52542b48446553babc42e4baae658e27" target="_blank">百度统计</a>

        </p>
 </div>
  </div>
</div>
<!--script type="text/javascript">
  var cpro_id = "u1484730";
  var r_top = -660;
  var _pos=0;
  var gtop_top = 0;
  $(window).scrollTop($(window).scrollTop()+1);
$(function(){
	if($(window).width()>1024)
	{
		$(window).scroll(function()
		{
			var yy = $(this).scrollTop();
			var sep = 33;
			var pos = yy-35;
			if(pos-sep>0)
			{
				$("#ad_l").css({top:(pos+sep)+"px"});
				$("#ad_r").css({top:(pos+sep+r_top)+"px"});
				_pos=pos+sep;
			}
			else
			{
				$("#ad_l").css({top:"0px"});
				$("#ad_r").css({top:r_top+"px"});
				_pos=r_top;
			}
                       _pos = $(this).scrollTop()-580+gtop_top;
                      // $("#gtop").css({top:_pos +"px"});
		});
	}
	else 
	{
		$('#ad_couplet').remove();
	}
}); 

</script>
<div style="margin:0 auto; width:980px; padding:0;" id="ad_couplet">
  <div style="position: absolute; top:10px; width:0;margin:0;padding:0;">
    <div style="left: -170px; height: 660px; overflow: hidden; position: relative; width: 160px; top: 0px;" id="ad_l">
	  <script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
      <div style="background-color:#fff" onclick="$('#ad_l').css('display','none');r_top=0;$('#ad_r').css({top:_pos+'px'});">关闭广告</div>
    </div>
    <div style="left: 990px; top: -660px; height: 620px; overflow: hidden; position: relative; width: 160px;" id="ad_r">
       <script type="text/javascript">
        var cpro_id = "u1484730";
       </script>
      <script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
      <div style="background-color:#fff" onclick="$('#ad_r').css('display','none');">关闭广告</div>
    </div>
<div id="gtop" style="position: fixed;top:670px;left:180px;width:30px;height:35px;"><a href="#top" target="_self"><img src="/templates/ttmeiju/images/scrollTop.jpg" /></a></div>
  </div>
</div-->

<script type="text/javascript">
    /*120*300 两侧对联*/
var cpro_id = "u2103825";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/f.js" type="text/javascript"></script>


<!--div style="position:fixed;top:150px; right:10px;" id="rightad">
  <img src="http://pic.yupoo.com/ttmeiju/EInMRzwt/medish.jpg" usemap="#Map234">
  <map name="Map234">
    <area shape="rect" coords="1,305,130,330" href="javascript:void()" onclick="$('#rightad').hide()">
    <area shape="rect" coords="1,1,130,305" href="http://um0.cn/536c2">
  </map>
</div-->
<!--footer end-->
"""

#re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
#re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
#re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
#re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
#re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
#re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

pattern = re.compile(r'<a[^>]*?>.+?演绎法.+?[^>]*?<\/a>', re.S) 
#pattern = re.compile(r'(?<=href=").*pan\.baidu\.com.+?(?="\s)') #匹配百度盘
matchList = re.findall(pattern, html)
if matchList:
    print "\n".join(matchList)
    print "length : " + str(len(matchList))
else:
    print "没有匹配"
