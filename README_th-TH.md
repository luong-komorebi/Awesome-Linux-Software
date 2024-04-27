<!-- markdown-link-check-disable -->

# ซอฟต์แวร์ลินุกซ์ สุดเจ๋ง

![Tux](img/tux.png)

🐧 This repo is a collection of **AWESOME** Linux applications and tools for **any users/developers**.
<br>
🐧 Feel free to **contribute** / **star** / **fork** / **pull request** . Any **recommendations** and **suggestions** are welcome.

**Acknowledgement:** _Everything written below is from my own experience in college and after reading various materials. I am neither a professional nor an expert, but a passionate student. Anyone can open a discussion in the issue section, or a pull request if something should be modified or added._

- ภาษาโปรตุเกส บราซิล : [ที่นี่](https://github.com/LewisVo/Awesome-Linux-Software/blob/master/README_pt-BR.md).
- ภาษาจีน : [ที่นี่](https://github.com/LewisVo/Awesome-Linux-Software/blob/master/README_zh-CN.md) หรือ [ที่นี่](https://github.com/alim0x/Awesome-Linux-Software-zh_CN) or [here](https://github.com/0xE8551CCB/awesome-linux-software-cn).
- ภาษาสเปน : [ที่นี่](https://github.com/LewisVo/Awesome-Linux-Software/blob/master/README_es-ES.md) หรือ [ที่นี่](https://github.com/SaintFenix/Awesome-Linux-Software/blob/master/README_es-ES.md)

## สารบัญ

- [แอปพลิเคชัน](#applications)
  - [เสียง](#audio)
  - [โปรแกรมสนทนา](#chat-clients)
  - [สำรองข้อมูลและกู้คืน](#data-backup-and-recovery)
  - [ปรับแต่งเดสก์ท็อป](#desktop-customization)
  - [พัฒนาซอฟต์แวร์](#development)
  - [เครื่องมือ E-Book](#e-book-utilities)
  - [แก้ไขข้อความ](#editors)
  - [การศึกษา](#education)
  - [เครื่องมือ Email](#email)
  - [จัดการไฟล์](#file-manager)
  - [เกมส์](#games)
  - [กราฟิก](#graphics)
  - [อินเทอร์เน็ต](#internet)
  - [สำนักงาน](#office)
  - [Productivity](#productivity)
  - [Proxy](#proxy)
  - [ความปลอดภัย](#security)
  - [แบ่งปันไฟล์](#sharing-files)
  - [เทอร์มินัล](#terminal)
  - [เครื่องไม้เครื่องมือ](#utilities)
  - [วิดีโอ](#video)
  - [ซอฟต์แวร์ Wiki](#wiki-software)
  - [อื่นๆ](#others)
- [Command Line Utilities](#command-line-utilities)
- [สภาพแวดล้อมเดสก์ท็อป](#desktop-environments)
- [ตัวจัดการ การแสดงผลหน้าจอ](#display-manager)
  - [Console](#console)
  - [Graphic](#graphic)
- [ตัวจัดการหน้าต่าง](#window-managers)
  - [Compositors](#compositors)
  - [Stacking window managers](#stacking-window-managers)
  - [Tiling window managers](#tiling-window-managers)
  - [Dynamic window managers](#dynamic-window-managers)

---

- [ติดตั้ง](#setup)
  - [ArchLinux](#arch-linux)
  - [Bodhi](#bodhi)
  - [CentOS](#centos)
  - [Fedora](#fedora)
  - [openSUSE](#opensuse)
  - [Ubuntu](#ubuntu)
- [กระทู้สนทนา](#discussion-forums)
  - [ArchLinux Forums](#arch-linux-forums)
  - [CentOS Forums](#centos-forums)
  - [Fedora Forums](#fedora-forums)
  - [Ubuntu Forums](#ubuntu-forums)
  - [openSUSE Forums](#opensuse-forums)
  - [IRC channels](#irc-channels)
  - [Linux News, Apps, and more ....](#linux-news-apps-and-more-)
  - [Reddit](#reddit)
- [เรียนรู้ลินุกซ์](#learn-linux)
- [Linux Hacking/Development](#linux-hackingdevelopment)
- [Advanced Linux](#advanced-linux)
- [แหล่งรวมของเจ๋งอื่นๆ](#other-awesome-lists)
- [Contributors](#contributors)
- [Guidelines to Contribute](#guidelines-to-contribute)
- [How to Contribute](#unsure-how-to-contribute)

---

## Applications

### Audio

_สำหรับแหล่งทรัพยากรในหมวดหมู่นี้ ที่ครอบคลุมกว่า/ขั้นสูงกว่า/ดีกว่า ด้านเสียงในลินุกซ์ คุณอาจสนใจ [ที่นี่](https://github.com/nodiscc/awesome-linuxaudio)_

- [![Open-Source Software][oss icon]](https://github.com/sourcefabric/Airtime) [Airtime](https://www.sourcefabric.org/software/airtime) - The open broadcast software for scheduling and remote station management
- [![Open-Source Software][oss icon]](https://ardour.org/development.html) [Ardour](https://ardour.org/) - บันทึก, แก้ไข, และมิกซ์ บนลินุกซ์
- [![Open-Source Software][oss icon]](http://audacious-media-player.org/developers) [Audacious](http://audacious-media-player.org/) - ตัวเล่นไฟล์เสียงที่เป็นโอเพนซอร์ส ที่กินทรัพยากรเครื่องของคุณน้อยมากๆ
- [![Open-Source Software][oss icon]](https://github.com/audacity/audacity) [Audacity](http://www.audacityteam.org/download/linux/) - ซอฟต์แวร์แก้ไขตัดต่อไฟล์เสียง ฟรีและโอเพนซอร์ส รองรับหลายระบบปฏิบัติการ
- [![Open-Source Software][oss icon]](https://bazaar.launchpad.net/~audio-recorder/audio-recorder/trunk/files) [Audio Recorder](https://launchpad.net/~audio-recorder) - โปรแกรมบันทึกเสียงอย่างง่าย ซึ่งอยู่ใน Ubuntu PPA
- [![Open-Source Software][oss icon]](https://github.com/Superjo149/auryo) [Auryo](http://auryo.com/) - แอปสำหรับใช้ SoundCloud® โดยนักพัฒนาอิสระ รองรับหลากหลายระบบปฏิบัติการสำหรับเดสก์ท็อป
- [![Open-Source Software][oss icon]](https://github.com/CDrummond/cantata) [Cantata](https://www.linux-apps.com/content/show.php/Cantata?content=147733) - โปรแกรมเล่นไฟล์เสียงผ่าน MPD (Music Player Daemon) สำหรับ ลินุกซ์, วินโดวส์, แมคโอเอส
- [![Open-Source Software][oss icon]](https://github.com/clementine-player/Clementine) [Clementine](https://www.clementine-player.org/) - โปรแกรมเล่นไฟล์เพลงความละเอียดสูง และรองรับไฟล์เสียงหลายรูปแบบ
- [![Open-Source Software][oss icon]](https://github.com/cmus/cmus) [Cmus](https://cmus.github.io/#download) - โปรแกรมเล่นไฟล์เสียงแบบเท็กซ์โหมดบนคอนโซล ที่เล็ก, เร็ว และประสิทธิภาพสูง บนระบบปฏิบัติการแบบ Unix-like
- [![Open-Source Software][oss icon]](https://github.com/linuxdeepin/deepin-music) [Deepin Music](https://www.deepin.org/en/original/deepin-music/) - แอปพลิเคชั่นที่พัฒนาโดยทีม Deepin Technology ที่มุ่งเน้นการเล่นไฟล์บนเครื่องของเรา
- [![Open-Source Software][oss icon]](https://github.com/enzo1982/freac) [fre:ac](https://www.freac.org/index.php) - fre:ac คือโปรแกรมแปลงไฟล์เสียงและแปลงแผ่น CD เป็นไฟล์เสียง ที่รองรับไฟล์เสียงหลายรูปแบบ ประกอบด้วย MP3, MP4/M4A, WMA, Ogg Vorbis, FLAC, AAC, WAV และ Bonk
- ![Open-Source Software][oss icon] [Gnormalize](http://gnormalize.sourceforge.net/) - โปรแกรมแปลงไฟล์เสียงและแปลง CD เป็นไฟล์เสียง โดยใช้ ReplayGain normalization algorithms, รวมถึงใช้เป็นตัวแก้ไข metadata (tag) และเป็นตัวเล่นไฟล์เสียงได้อีกด้วย โดยใช้ gtk2-perl ภายใต้ GNU/Linux
- [![Open-Source Software][oss icon]](https://github.com/MarshallOfSound/Google-Play-Music-Desktop-Player-UNOFFICIAL-) [Google Play Music](https://www.googleplaymusicdesktopplayer.com/) - โปรแกรมสำหรับเล่นเพลงจาก Google Play Music โดยนักพัฒนาภายนอก รองรับหลายระบบปฏิบัติการสำหรับเครื่องเดสก์ท็อป
- [![Open-Source Software][oss icon]](https://github.com/gpodder/gpodder) [Gpodder](https://gpodder.github.io/) - โปรแกรมสำหรับฟัง podcast และรวบรวมไฟล์มีเดียต่างๆ
- [![Open-Source Software][oss icon]](https://github.com/haecker-felix/gradio/releases/) [GRadio](https://github.com/haecker-felix/gradio/releases/) - ซอฟต์แวร์ที่เกียวข้องกับวิทยุสำหรับ Ubuntu Linux
- [![Open-Source Software][oss icon]](https://github.com/mtytel/helm) [Helm](http://tytel.org/helm/) - ซอฟต์แวร์สำหรังสังเคราะห์เสียง สามารถใช้ได้ทั้งแบบ stand alone และเป็นแบบปลั๊กอิน LV2, VST, VST3 และ AU
- [![Open-Source Software][oss icon]](https://github.com/hydrogen-music/hydrogen) [Hydrogen](http://hydrogen-music.org/) - เครื่องมือสำหรับกลองขั้นสูงสำหรับ GNU/Linux
- [![Open-Source Software][oss icon]](https://github.com/trazyn/ieaseMusic) [ieaseMusic](https://github.com/trazyn/ieaseMusic) - iEaseMusic is a multiplatform program built in electron for listening to NetEase Music.
- [![Open-Source Software][oss icon]](https://github.com/KDE/k3b) [K3b](http://www.k3b.org/) - โปรแกรมสำหรับสร้างแผ่น CD/DVD สำหรับลินุกซ์ ปรับแต่งให้เข้ากันกับ KDE
- [![Open-Source Software][oss icon]](https://kid3.sourceforge.io/) [Kid3Qt](https://apps.ubuntu.com/cat/applications/precise/kid3-qt/) - แก้ไขข้อมูล tag ได้ทีละหลายๆ ไฟล์ เช่น ศิลปิล, อัลบั้ม, ปีที่ออก และ แนวเพลง สำหรับไฟล์ mp3
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/kxstudio/) [KxStudio](http://kxstudio.linuxaudio.org/) - รวบรวมโปรแกรมและส่วนเสริมสำหรับผู้ที่ทำงานด้านเสียงมืออาชีพ
- [![Open-Source Software][oss icon]](https://github.com/LibreTime/libretime) [Libretime](http://libretime.org/) - ซอฟต์แวร์สำหรับทำสถานีกระจายเสียง จัดตารางและควบคุมระยะไกล ซอฟต์แวร์ต้นแบบมาจาก Airtime
- [![Open-Source Software][oss icon]](https://github.com/LMMS/lmms) [LMMS](https://lmms.io/download/#linux) - สร้างดนตรีบนเครื่องคอมพิวเตอร์ของคุณ โดยสร้างเมโลดี้และจังหวะ, สังเคราะห์เสียง ผสมเสียง รวมถึงเรียบเรียงและอีกมากมาย
- [![Open-Source Software][oss icon]](https://github.com/gnumdk/lollypop) [Lollypop](https://wildskyf.github.io/lollypop-web/) - โปรแกรมเล่นเพลงของ GNOME
- [![Open-Source Software][oss icon]](https://github.com/emilioastarita/lyricfier) [Lyricfier](https://github.com/emilioastarita/lyricfier) - โปรแกรมแสดงเนื้อเพลงที่เล่นผ่าน Spotify
- [![Open-Source Software][oss icon]](https://github.com/mixxxdj/mixxx) [Mixxx](http://www.mixxx.org/download/) - ซอฟต์แวร์ DJ ฟรี ที่มีทุกสิ่งสำหรับแสดงการมิกซ์สด โดยให้อารมณ์ใกล้เคียงโปรแกรม Traktor
- [![Open-Source Software][oss icon]](https://github.com/ColinDuquesnoy/MellowPlayer) [Mellow Player](https://colinduquesnoy.github.io/MellowPlayer/) - เชื่อมต่อเพลงบนคลาวด์กับเครื่องเดสก์ท็อปของคุณ
- [![Open-Source Software][oss icon]](https://github.com/mopidy/mopidy) [Mopidy](https://www.mopidy.com/) - ซอฟต์แวร์ music server พัฒนาด้วยภาษา Python
- [![Open-Source Software][oss icon]](https://github.com/KeitIG/museeks) [Museek](http://museeks.io/) - โปรแกรมเล่นเพลงอย่างง่าย รองรับหลายระบบปฏิบัติการ
- [![Open-Source Software][oss icon]](https://github.com/musescore/MuseScore) [MuseScore](https://musescore.org) - Create, play and print beautiful sheet music.
- [![Open-Source Software][oss icon]](https://github.com/metabrainz/picard) [MusicBrainz Picard](https://picard.musicbrainz.org/) - Picard คือซอฟต์แวร์แก้ไขแท็คของไฟล์เสียง พัฒนาโดยใช้ภาษา Python รองรับหลายระบบปฏิบัติการ
- [![Open-Source Software][oss icon]](https://about.musixmatch.com/apps/) [MusixMatch](https://about.musixmatch.com/apps/) - A Capable lyrics app with synchronized lyrics function.
- [Netease Music](http://music.163.com/#/download) - โปรแกรมมเล่นเพลงสำหรับ Netease - ผู้ให้บริการเพลงบนคลาวด์ในประเทศจีน
- [![Open-Source Software][oss icon]](https://github.com/nukeop/nuclear) [Nuclear](http://nuclear.gumblert.tech/) - โปรแกรมเล่นเพลงที่ถูกเขียนมาจาก Electron, รองรับหลายระบบปฏิบัติการ ที่สามารถเล่นเพลงผ่านเครือข่ายได้หลายแหล่ง
- [Ocenaudio](http://www.ocenaudio.com/whatis) - โปรแกรมแก้ไขตัดต่อไฟล์เสียงที่เหมาะสำหรับผู้ที่ต้องการวิเคราะห์ไฟล์เสียง
- [![Open-Source Software][oss icon]](https://github.com/PedroHLC/osdlyrics) [OSD Lyrics](https://aur.archlinux.org/packages/osdlyrics-git/) - แสดงเนื้อเพลงจากโปรแกรมเล่นเพลงโปรดของคุณ
- [![Open-Source Software][oss icon]](https://github.com/gkarsay/parlatype) [Parlatype](http://gkarsay.github.io/parlatype/) - GNOME ซอฟต์แวร์เล่นไฟล์เสียงจาก GNOME สำหรับถอดไฟล์เสียง
- [![Open-Source Software][oss icon]](https://github.com/pithos/pithos) [Pithos](https://pithos.github.io/) - โปรแกรมสำหรับเล่นเพลงผ่าน Pandora สำหรับลินุกซ์
- [![Open-Source Software][oss icon]](https://github.com/wwmm/pulseeffects) [PulseEffect](https://github.com/wwmm/pulseeffects) - Limiter, compressor, reverberation, equalizer and auto volume effects for Pulseaudio applications.
- [![Open-Source Software][oss icon]](https://github.com/quodlibet/quodlibet) [Quod Libet](https://quodlibet.readthedocs.io) - GTK+ music player written with huge libraries in mind. Supports search-based dynamic playlists, regular expressions, tagging, Replay Gain, podcasts & Internet radio.
- [![Open-Source Software][oss icon]](https://github.com/ebruck/radiotray-ng) [RadioTray-NG](https://github.com/ebruck/radiotray-ng) - โปรแกรมเล่นวิทยุออนไลน์สำหรับลินุกซ์
- [![Open-Source Software][oss icon]](https://github.com/GNOME/rhythmbox) [Rhythmbox](https://wiki.gnome.org/Apps/Rhythmbox) - โปรแกรมเล่นเพลง พัฒนาโดย GNOME
- [![Open-Source Software][oss icon]](https://sayonara-player.com/downloads/#Source) [Sayonara Player](https://sayonara-player.com/downloads/) - โปรแกรมเล่นไฟล์เสียง ขนาดกะทัดรัด และทำงานได้รวดเร็ว สำหรับลินุกซ์ พัฒนาโดยภาษา C++ และรองรับ Qt
- [![Open-Source Software][oss icon]](https://launchpad.net/soundconverter/trunk/2.1.6) [Soundconverter](http://soundconverter.org/) - ผู้นำด้านการแปลงไฟล์เสียง โดยมีจุดหมายคือทำให้ใช้ง่ายและทำงานได้รวดเร็ว
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/SoundJuicer) [SoundJuicer](http://www.howtogeek.com/howto/20126/rip-audio-cds-with-sound-juicer/) - เครื่องมือแปลง CD เป็นไฟล์เสียงสำหรับ GNOME
- [![Open-Source Software][oss icon]](https://github.com/Soundnode/soundnode-app) [Soundnode](https://soundnode.github.io/soundnode-website/) - โปรแกรมเล่น SoundCloud บนเดสก์ท็อป
- [![Open-Source Software][oss icon]](https://github.com/devinhalladay/spotio) [Spotio](https://github.com/devinhalladay/spotio) - เปลี่ยนหน้าตาของโปรแกรม Spotify ให้เป็นรูปแบบคล้าย Rdio
- [![Open-Source Software][oss icon]](https://github.com/VCVRack/Rack) [VCV Rack](https://vcvrack.com/) - An open-source virtual modular synthesizer.
- [![Open-Source Software][oss icon]](https://github.com/needle-and-thread/vocal) [Vocal](http://vocalproject.net/) - โปรแกรมเล่น Podcast สำหรับเดสก์ท็อปยุคใหม่

### Chat Clients

#### 3rd party Client

- [![Open-Source Software][oss icon]](https://github.com/sindresorhus/caprine) [Caprine](https://sindresorhus.com/caprine) - โปรแกรมแชท Facebook Messenger บนเดสก์ท็อป หน้าตาสวยงาม
- [![Open-Source Software][oss icon]](https://github.com/chatty/chatty) [Chatty](http://chatty.github.io/) - Chatty คือโปรแกรมสำหรับสนทนาบน Twitch ซึ่งเป็นได้มากกว่าการสนทนาผ่านเว็บแบบปกติ แต่ไม่ถึงกับต้องมีฟีเจอร์เท่าโปรแกรม IRC ทั่วไป
- [![Open-Source Software][oss icon]](https://github.com/stanfieldr/ghetto-skype) [GhettoSkype](https://github.com/stanfieldr/ghetto-skype) - เป็นเว็บสำหรับใช้ Skype
- [![Open-Source Software][oss icon]](https://github.com/Aluxian/Facebook-Messenger-Desktop) [Messenger for Desktop](https://messengerfordesktop.com/#download) - แอปสำหรับใช้ Facebook messenger
- [![Open-Source Software][oss icon]](https://github.com/raelgc/scudcloud/) [ScudCloud](https://github.com/raelgc/scudcloud/) - โปรแกรมสำหรับใช้ Slack บนลินุกซ์
- [![Open-Source Software][oss icon]](https://github.com/yakyak/yakyak) [YakYak](https://github.com/yakyak/yakyak) - โปรแกรมสนทนา Google Hangouts บนเดสก์ท็อป

#### All-in-One Client

- [![Open-Source-Software][oss icon]](https://github.com/meetfranz/franz) [Franz](http://meetfranz.com/) - Franz แอปส่งข้อความฟรี โดยรวมทั้งการสนทนาและการส่งข้อความอยู่ในแอปพลิเคชันเดียว
- [![Open-Source Software][oss icon]](https://developer.pidgin.im/) [Pidgin](https://pidgin.im/) - โปรแกรมสนทนาครอบจักรวาล
- [![Open-Source Software][oss icon]](https://github.com/saenzramiro/rambox) [Rambox](http://rambox.pro/) - แพลตฟอร์มสำหรับส่งข้อความและอีเมล โดยรวมความสามารถของเว็บแอปต่างๆ เข้ามาเป็นหนึ่งเดียว

#### Chat Client Utilities

- [![Open-Source Software][oss icon]](https://github.com/Cog-Creators/Red-DiscordBot) [Red Discord Bot](https://index.discord.red/) - Red Discord Bot คือซอฟต์แวร์สำหรับทำระบบบอตเกี่ยวกับ เพลง/สนทนา/และอื่นๆ ซึ่งสามารถใช้ได้บน Raspberry Pi และระบบปฏิบัติการอื่นๆ โดยสามารถเพิ่มความสามารถได้ผ่านระบบที่เรียกว่า "Cogs"

#### IRC Client

- [![Open-Source Software][oss icon]](https://github.com/hexchat) [HexChat](https://hexchat.github.io/) - HexChat โปรแกรมสนทนาบนเครือข่าย IRC โดยมีฐานมาจากโปรแกรม XChat สามารถใช้ได้กับทั้ง Windows และ ระบบตระกูล Unix ทั้งหลาย
- [![Open-Source Software][oss icon]](https://github.com/irssi/irssi) [Irssi](https://github.com/irssi/irssi) - Irssi คือโปรแกรมสนทนาที่มีชื่อเสียงในด้าน เป็นโปรแกรมสนทนาที่มีส่วนหน้าจอติดต่อผู้ใช้เป็นโหมดข้อความ
- [![Open-Source Software][oss icon]](https://github.com/kvirc/KVIrc) [KVIrc](http://www.kvirc.net/) - KVIrc คือโปรแกรมสนทนา IRC สร้างจาก Qt

#### Official Client

- [![Open-Source-Software][oss icon]](hhttps://sourceforge.net/p/beebeep/code/HEAD/tree/) [BeeBEEP](http://beebeep.sourceforge.net) - BeeBEEP is an open source, peer to peer, lan messenger. You can talk and share files with anyone inside your local area network. You don't need a server, just download, unzip and start it. Simple, fast and secure.
- [![Open-Source Software][oss icon]](https://github.com/dino/dino) [Dino](https://dino.im) - โปรแกรมสนทนาบน Jabber/XMPP ที่สวยงามเรียบง่าย
- [Discord](https://discordapp.com/) - โปรแกรมหลากหลายฟังก์ชัน ทั้งข้อความและเสียง สำหรับนักเล่นเกม ที่ฟรี ปลอดภัย และใช้ได้ทั้งเดสก์ท็อปและโทรศัพท์มือถือ
- [![Open-Source Software][oss icon]](https://github.com/gitterHQ/services) [Gitter](https://gitter.im/) - Gitter — ที่ๆ ซึ่งนักพัฒนามาสนทนากัน Gitter ถูกออกแบบเพื่อให้เข้ากับการสนทนาระดับชุมชน การทำงานร่วมกัน โดยต้องให้ใช้งานได้ง่ายและลื่นไหลที่สุด
- [![Open-Source Software][oss icon]](https://github.com/jitsi) [Jitsi](https://jitsi.org/) - Jitsi คือซอฟต์แวร์สำหรับการประชุมทางไกล และ สนทนาแบบทันใจ สำหรับ Windows ลินุกซ์ Mac OS X และ แอนดรอยด์
- [![Open-Source Software][oss icon]](https://github.com/qTox/qTox) [qTox](https://qtox.github.io/) - ซอฟต์แวร์สำหรับสนทนาด้วยเสียงและวิดีโอแบบกระจายศูนย์ที่ปลอดภัย
- [![Open-Source Software][oss icon]](https://ring.cx/en/documentation/faq#node-106) [Ring](https://ring.cx/) - สนทนา พูดคุย แบ่งปัน Ring คือซอฟต์แวร์แพลตฟอร์มสำหรับการสนทนาที่ปลอดภัยและมีเสรีภาพ
- [![Open-Source Software][oss icon]](https://github.com/vector-im/riot-web) [Riot](https://riot.im/) - เว็บแอปสำหรับสื่อสาร เน้นการทำงานร่วมกัน โดยอยู่บนเครือข่าย Matrix
- [Skype](https://www.skype.com/en/) - Skype ทำให้ทั้งโลกได้สนทนากัน แบบฟรีๆ
- [Slack](https://slack.com/downloads/linux) - สนทนาพูดคุยกันแบบทันใจ เก็บและค้นหาข้อความต่างๆ สำหรับทีมสมัยใหม่
- [![Open-Source Software][oss icon]](https://github.com/telegramdesktop/tdesktop) [Telegram](https://desktop.telegram.org/) - ซอฟต์แวร์สนทนาที่เน้นทางด้าน ความเร็ว และ ความปลอดภัย และสามารถใช้ได้ฟรี
- [Viber](https://www.viber.com/en/products/linux) - Viber สำหรับ ลินุกซ์ ให้คุณได้ส่งข้อความและโทรหาผู้ใช้ Viber คนอื่นได้ฟรี ทุกอุปกรณ์และเครือข่าย ทุกประเทศ
- [![Open-Source Software][oss icon]](https://github.com/weechat) [Weechat](https://weechat.org/) - WeeChat คือซอฟต์แวร์สนทนาที่ทำงานได้เร็ว เล็กกระทัดรัด และเพิ่มเติมความสามารถได้
- [![Open-Source Software][oss icon]](https://github.com/wireapp) [Wire](https://wire.com/en/) - สื่อสารอย่างปลอดภัย และรักษาความเป็นส่วนตัว

### Data Backup and Recovery

- [![Open-Source Software][oss icon]](https://borgbackup.readthedocs.io/en/stable/development.html) [Borg Backup](https://borgbackup.readthedocs.io/en/stable/) - เครื่องมือสำรองข้อมูลที่น่าใช้
- [![Open-Source Software][oss icon]](https://launchpad.net/deja-dup) [Deja Dup](https://www.linux.com/learn/total-system-backup-and-recall-deja-dup) - เครื่องมือสำรองข้อมูลอย่างง่าย ที่รองรับการเข้ารหัสข้อมูลในตัว
- [![Open-Source Software][oss icon]](https://launchpad.net/duplicity) [Duplicity](http://duplicity.nongnu.org/) - Duplicity สำรองข้อมูลทั้งไดเรกทอรี่ไว้ที่เครื่องเราเองหรือเซอร์ฟเวอร์อื่นๆ โดยเข้ารหัสในรูปแบบ tar
- [![Open-Source Software][oss icon]](https://www.freefilesync.org/download.php) [FreeFileSync](https://www.freefilesync.org) - FreeFileSync is a folder comparison and synchronization software that creates and manages backup copies of all your important files. Instead of copying every file every time, FreeFileSync determines the differences between a source and a target folder and transfers only the minimum amount of data needed.
- [![Open-Source Software][oss icon]](https://github.com/cgsecurity/testdisk) [Photorec](http://www.cgsecurity.org/wiki/PhotoRec) - PhotoRec คือซอฟต์แวร์กู้คืนไฟล์ โดยออกแบบมาสำหรับกู้คืนข้อมูลต่างๆ รวมไปถึงไฟล์วิดีโอ เอกสารและไฟล์ต่างๆ ในฮาร์ดดิสก์, แผ่นซีดีและไฟล์รูปภาพที่หายไป (ซึ่งเป็นที่มาของชื่อ Photo Recovery) จากหน่วยความจำในกล้องถ่ายรูป
- [![Open-Source Software][oss icon]](https://borgbackup.readthedocs.io/en/stable/) [Qt4-fsarchiver](https://sourceforge.net/projects/qt4-fsarchiver/) - qt4-fsarchiver คือเครื่องมือสำรองและเรียกคืน พาร์ทิชันของดิสก์ โฟลเดอร์ หรือแม้กระทั่งตาราง MBR/GPT โดยโปรแกรมนี้รองรับระบบ Debian, OpenSuse และ Fedora
- [![Open-Source Software][oss icon]](https://github.com/ncw/rclone) [rclone](http://rclone.org/) - Rclone คำโปรแกรมบรรทัดคำสั่งสำหรับซิงค์ไฟล์และไดเรกทอรี่ ทั้งจากและไปยัง พื้นที่เก็บไฟล์บนคลาวด์ต่างๆ และยังสามารถเข้ารหัสข้อมูลที่สำรองได้อีกด้วย
- [![Open-Source Software][oss icon]](https://github.com/rsnapshot/rsnapshot.git) [rsnapshot](http://rsnapshot.org/) - rsnapshot เครื่องมือคำสั่งโดยมี rsync เป็นฐาน ซึ่งทำหน้าที่ snapshot เป็นช่วงเวลา ทั้งเครื่องเราเองและเครื่องรีโมทอื่นๆ ตัวโค้ดใช้ hard link ทุกที่ๆ เป็นไปได้ เพื่อลดการใช้เนื้อที่ในดิสก์
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/systemrescuecd/files/sysresccd-x86/) [System Rescue CD](http://www.system-rescue-cd.org/SystemRescueCd_Homepage) - SystemRescueCd คือลินุกซ์ที่สำหรับกู้ชีพเครื่องคอมพิวเตอร์ สามารถบูตได้ผ่านแผ่นซีดีหรือแฟลชไดรฟ์ USB
- [![Open-Source Software][oss icon]](https://github.com/cgsecurity/testdisk) [Test Disk](http://www.cgsecurity.org/wiki/TestDisk) - TestDisk คือซอฟต์แวร์กู้ข้อมูลประสิทธิภาพสูง ซึ่งออกแบบมาเพื่อกู้คืนพาร์ทิชันที่เสียหายเป็นหลัก และทำให้ดิสก์สามารถกลับมาบูตใหม่ได้อีกครั้ง
- [![Open-Source Software][oss icon]](https://code.launchpad.net/timeshift) [Timeshift](https://launchpad.net/timeshift) - TimeShift คือเครื่องมือย้อนคืนระบบ โดยทำ snapshot ระบบ เก็บไว้เป็นระยะ โดยใช้ rsync และ hard-link โดย snapshot เหล่านี้สามารถย้อนคืนกลับได้ทีหลัง ซึ่งสิ่งที่เปลี่ยนแปลงไปหลังจาก snapshot จะไม่ถือว่าเกิดขึ้น โดย snapshot สามารถสร้างได้เองหรือกำหนดช่วงวันเวลาที่ต้องการสร้างได้

### Desktop Customization

#### Desktop Themes

- [![Open-Source Software][oss icon]](https://github.com/adapta-project/adapta-gtk-theme) [Adapta Theme](https://github.com/tista500/Adapta) - An adaptive Gtk+ theme based on Material Design Guidelines.
- [![Open-Source Software][oss icon]](https://github.com/EliverLara/Ant) [Ant Theme](http://www.omgubuntu.co.uk/2017/09/ant-flat-gtk-theme-bloody-bite) - Ant is a flat GTK theme for Ubuntu and other GNOME-based Linux desktops it comes in three varieties: vanilla, Bloody, or Dracula.
- [![Open-Source Software][oss icon]](https://github.com/jnsh/arc-theme) [Arc Theme](https://github.com/jnsh/arc-theme) - A flat theme with transparent elements
- [![Open-Source Software][oss icon]](https://github.com/solus-project/evopop-gtk-theme) [EvoPop Theme](https://github.com/solus-project/evopop-gtk-theme) - EvoPop is a modern desktop theme suite build for the Solus Project. Its design is mostly flat with a minimal use of shadows for depth.
- [![Open-Source Software][oss icon]](https://github.com/andreisergiu98/arc-flatabulous-theme) [Flatabulous Arc Theme](https://github.com/andreisergiu98/arc-flatabulous-theme) - A flat and blue GTK theme that also comes in darker versions.
- [![Open-Source Software][oss icon]](https://github.com/anmoljagetia/Flatabulous) [Flatabulous](https://github.com/anmoljagetia/Flatabulous) - This is a Flat theme for Ubuntu and other Gnome based Linux Systems.
- [![Open-Source Software][oss icon]](https://github.com/bsundman/Irradiance) [Irradiance Theme](https://github.com/bsundman/Irradiance) - A Unity theme inspired by OSX Yosemite based on Radiance.
- [![Open-Source Software][oss icon]](https://github.com/numixproject/numix-gtk-theme) [Numix Theme](https://itsfoss.com/install-numix-ubuntu/) - A flat and colorful GTK-Theme.
- [![Open-Source Software][oss icon]](https://github.com/bsundman/Yosembiance) [Yosembiance theme](https://github.com/bsundman/Yosembiance) - A modified Ambiance theme (loosely) inspired by OSX Yosemite.

#### Desktop Widgets and Theme Utilities

- [![Open-Source Software][oss icon]](https://launchpad.net/compizconfig-settings-manager) [Compiz Config settings manager](https://apps.ubuntu.com/cat/applications/compizconfig-settings-manager/) - The OpenCompositing Project brings 3D desktop visual effects that improve usability of the X Window System and provide increased productivity.
- [![Open-Source Software][oss icon]](https://github.com/brndnmtthws/conky) [Conky](https://github.com/brndnmtthws/conky) - Conky is a free, light-weight system monitor for X, that displays any kind of information on your desktop.
- [Gnome Extensions](http://extensions.gnome.org/) - Extensions for the Gnome Desktop Environment.
- [Gnome Look](https://www.gnome-look.org/) - A website that hosts a Large amounts of community created icons, shell themes, fonts, and many more assets that can be used to customize your Gnome desktop environment.
- [![Open-Source Software][oss icon]](https://github.com/bil-elmoussaoui/Hardcode-Tray) [Hardcode Tray](https://github.com/bil-elmoussaoui/Hardcode-Tray) - This script fixes hardcoded tray icons in Linux by automatically detecting your default theme, the right icon size, the hard-coded applications, the right icons for each indicator and fix them.
- [Macbuntu](http://www.noobslab.com/2017/06/macbuntu-transformation-pack-ready-for.html) - A transformation pack for making your desktop look like a macOS.
- [![Open-Source Software][oss icon]](https://github.com/opendesktop/ocsstore) [OCS store](https://github.com/opendesktop/ocsstore) - Desktop app of openDesktop.org, which is one of the largest communities where developers and artists share applications, themes and other content.
- [![Open-Source Software][oss icon]](https://github.com/actionless/oomox) [Oomox theme generator](https://github.com/actionless/oomox) - A Graphical application for generating different color variations of a Numix-based and Flat-Plat themes (GTK2, GTK3), Gnome-Colors and Archdroid icons.
- [![Open-Source Software][oss icon]](https://github.com/jaagr/polybar) [Polybar](https://github.com/jaagr/polybar) - Fast and easy-to-use status bar.
- [![Open-Source Software][oss icon]](https://github.com/ianyh/Amethyst) [Unity Tweak Tool](https://apps.ubuntu.com/cat/applications/unity-tweak-tool/) - A Must-have app for Ubuntu Unity customization.
- [![Open-Source Software][oss icon]](https://github.com/deviantfero/wpgtk) [Wpgtk](http://deviantfero.github.io/wpgtk) - A universal theming software for all themes defined in text files, compatible with all terminals, with default themes for GTK2, GTK+, openbox and Tint2 that uses pywal as it's core for colorscheme generation.

#### Desktop Icon Packs

- [![Open-Source Software][oss icon]](https://github.com/horst3180/arc-icon-theme) [Arc Icon Theme](https://github.com/horst3180/arc-icon-theme) - A modern flat icon theme that builds on and requires the Moka Icon Theme to work.
- [![Open-Source Software][oss icon]](https://github.com/keeferrourke/la-capitaine-icon-theme) [La Capitaine Icon Theme](https://github.com/keeferrourke/la-capitaine-icon-theme) - A macOS and Material design inspired icon theme designed to fit into most desktop environments.
- [![Open-Source Software][oss icon]](https://github.com/snwh/moka-icon-theme) [Moka Icon Theme](https://snwh.org/moka) - Moka was created with simplicity in mind. With the use simple geometry & bright colours.
- [![Open-Source Software][oss icon]](https://github.com/numixproject/numix-icon-theme) [Numix Icon Theme](http://www.noobslab.com/2014/04/install-numix-icon-packs-in-ubuntulinux.html) - A flat icon theme that comes in two varieties, Numix Main, and Numix circle.
- [![Open-Source Software][oss icon]](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme-gtk/) [Papirus Icon Theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme-gtk/) - SVG icon theme for Linux systems, based on Paper with a few extras like (hardcode-tray support, kde-color-scheme support, libreoffice icon theme, filezilla theme, smplayer themes ...) and other modifications. The theme is available for GTK and KDE.

### Development

#### Android

- [![Open-Source Software][oss icon]](https://github.com/anbox/anbox) [Anbox](https://anbox.io) - Run Android applications on any GNU/Linux operating system.
- [Android studio](https://developer.android.com/studio/index.html) - The Official IDE for Android: Android Studio provides the fastest tools for building apps on every type of Android device.

#### C\+\+

- ![Non Free][money icon] [Clion](https://www.jetbrains.com/clion/) - A cross-platform and powerful IDE for C and C++! [Nonfree][money icon]
- [Code::Blocks](http://www.codeblocks.org/) - Code::Blocks is a free C, C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
- [Codelite](http://codelite.org/) - A Free, open source, cross platform C,C++,PHP and Node.js IDE.
- [![Open-Source Software][oss icon]](https://github.com/qt-creator/qt-creator) [QT Creator](https://www.qt.io/ide/) - Fully-stocked cross-platform integrated development environment for easy creation of connected devices, UIs and applications.

#### ฐานข้อมูล

- [![Open-Source Software][oss icon]](https://github.com/apache/cassandra) [Cassandra](http://cassandra.apache.org/) - Apache Cassandra database is the right choice when you need scalability and high availability without compromising performance. Linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure make it the perfect platform for mission-critical data.
- [![Open-Source Software][oss icon]](https://github.com/apache?query=couchdb) [CouchDB](http://couchdb.apache.org/) - Seamless multi-master sync, that scales from Big Data to Mobile, with an Intuitive HTTP/JSON API and designed for Reliability.
- [![Open-Source Software][oss icon]](https://github.com/serge-rider/dbeaver/) [DBeaver](http://dbeaver.jkiss.org/) - A universal database client supporting multiple platforms and databases.
- [![Open-Source Software][oss icon]](https://cgit.kde.org/kexi.git/about/) [Kexi](http://kexi-project.org/) - Kexi is an open source visual database applications creator, a long-awaited competitor for programs like MS Access or Filemaker.
- [![Open-Source Software][oss icon]](https://mariadb.org/get-involved/getting-started-for-developers/) [MariaDB](https://mariadb.org/) - One of the most popular database servers. Made by the original developers of MySQL.
- [![Open-Source Software][oss icon]](https://github.com/mongodb/mongo) [MongoDB](https://www.mongodb.com/) - MongoDB is a free and open-source cross-platform document-oriented database program, uses JSON-like documents with schemas.
- [![Open-Source Software][oss icon]](https://github.com/mysql/mysql-server) [MySQL](https://dev.mysql.com/doc/refman/5.7/en/linux-installation.html) - MySQL is the world's leading open source database thanks to its proven performance, reliability and ease-of-use. It is used by high profile web properties including Facebook, Twitter, YouTube, Yahoo! and many more.
- [![Open-Source Software][oss icon]](https://github.com/mysql/mysql-workbench) [MySQL Workbench](https://www.mysql.com/products/workbench/) - MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. MySQL Workbench provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, backup, and much more.
- [![Open-Source Software][oss icon]](https://github.com/dbcli/mycli) [MyCLI](http://www.mycli.net/) - MyCLI is a command line interface for MySQL, MariaDB, and Percona with auto-completion and syntax highlighting.
- [OmniDB](https://omnidb.org) - Browser-based tool that visually create, manage, and view databases.
- ![Non Free][money icon] [OracleDB](http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html) - Object-relational database management system produced and marketed by Oracle Corporation, one of the most trusted and widely-used relational database engines.
- [![Open-Source Software][oss icon]](https://github.com/percona/percona-server-mongodb) [Percona MongoDB](https://www.percona.com/software/mongo-database/percona-server-for-mongodb) - Percona Server for MongoDB provides all features and benefits of MongoDB Community Server.
- [![Open-Source Software][oss icon]](https://github.com/percona/pmm-server) [Percona Monitoring](https://www.percona.com/software/database-tools/percona-monitoring-and-management) - Percona Monitoring and Management (PMM) is a free and open-source platform for managing and monitoring MySQL, MariaDB and MongoDB performance. You can run PMM in your own environment for maximum security and reliability. It provides thorough time-based analysis for MySQL, MariaDB and MongoDB servers to ensure that your data works as efficiently as possible.
- [![Open-Source Software][oss icon]](https://github.com/percona/percona-server) [Percona MySQL](https://www.percona.com/software/mysql-database/percona-server) - Percona Server for MySQL is a free, fully compatible, enhanced, open source drop-in replacement for MySQL that provides superior performance, scalability and instrumentation.
- [![Open-Source Software][oss icon]](https://github.com/percona/percona-xtradb-cluster) [Percona XtraDB Cluster](https://www.percona.com/software/mysql-database/percona-xtradb-cluster) - Percona XtraDB Cluster is an active/active high availability and high scalability open source solution for MySQL clustering. It integrates Percona Server and Percona XtraBackup with the Codership Galera library of MySQL high availability solutions in a single package that enables you to create a cost-effective MySQL high availability cluster.
- [![Open-Source Software][oss icon]](https://github.com/dbcli/pgcli) [pgcli](https://www.pgcli.com/) - Pgcli is a command line interface for Postgres with auto-completion and syntax highlighting.
- [![Open-Source Software][oss icon]](https://github.com/postgres/postgres) [PostgreSQL](https://www.postgresql.org/download/) - PostgreSQL is a powerful, open source object-relational database system with more than 15 year development. PostgreSQL is not controlled by any corporation or other private entity and the source code is available free of charge
- [![Open-Source Software][oss icon]](https://www.sqlite.org/src/doc/trunk/README.md) [Sqlite](https://sqlite.org/download.html) - SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
- [![Open-Source Software][oss icon]](https://github.com/sqlitebrowser/sqlitebrowser) [Sqlite Browser](http://sqlitebrowser.org/) - Visually create, manage, and view sqlite database files.

#### Golang

- [GoLand](https://www.jetbrains.com/go/) - GoLand is the codename for a new commercial IDE by JetBrains aimed at providing an ergonomic environment for Go development.

#### Java

- [![Open-Source Software][oss icon]](https://www.bluej.org/versions.html) [BlueJ](http://bluej.org/) - A free Java Development Environment designed for beginners, used by millions worldwide.
- [Eclipse](https://eclipse.org/ide/) - Eclipse is famous for our Java Integrated Development Environment (IDE), but can also download packages to support C/C++ IDE and PHP IDE.
- [![Open-Source Software][oss icon]](https://github.com/JetBrains/intellij-community) [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Powerful IDE for JAVA. The Community version is open sourced.

#### Javascript

- [Webstorm](https://www.jetbrains.com/webstorm/) - Powerful IDE for modern JavaScript development, made by JetBrains.

#### Microcomputer and Embedded Devices

- [![Open-Source Software][oss icon]](https://github.com/arduino/arduino-ide) [Arduino IDE](https://www.arduino.cc/en/Main/Software) - The open-source Arduino Software (IDE) makes it easy to write code and upload it to the board.
- [![Open-Source Software][oss icon]](https://github.com/fritzing/fritzing-app) [Fritzing](http://fritzing.org/) - Fritzing is an open-source hardware initiative that makes electronics accessible as a creative material for anyone.
- [![Open-Source Software][oss icon]](https://github.com/jantje/arduino-eclipse-plugin) [Sloeber IDE](http://eclipse.baeyens.it/) - Sloeber IDE. The Arduino IDE for Eclipse.

#### Multiple Languages Support

- [![Open-Source Software][oss icon]](https://github.com/aptana) [Aptana](http://www.aptana.com/) - Aptana Studio harnesses the flexibility of Eclipse and focuses it into a powerful web development engine.
- [![Open-Source Software][oss icon]](https://phabricator.kde.org/dashboard/view/8/) [KDevelop](https://www.kdevelop.org/) - It is a free, open source IDE, feature-full, plugin extensible IDE for C/C++ and other programming languages.
- [![Open-Source Software][oss icon]](http://www.monodevelop.com/developers/) [MonoDevelop](http://www.monodevelop.com/) - Cross platform IDE for C#, F# and more.
- [![Open-Source Software][oss icon]](https://github.com/apache/netbeans) [Netbeans](https://netbeans.org/downloads/) - NetBeans IDE lets you quickly and easily develop Java desktop, mobile, and web applications, as well as HTML5 applications with HTML, JavaScript, and CSS.

#### PHP

- [PHPStorm](https://www.jetbrains.com/phpstorm/) - Lightning-smart and powerful PHP IDE from Jetbrain.

#### Python

- [![Open-Source Software][oss icon]](https://github.com/JetBrains/intellij-community/tree/master/python) [PyCharm](https://www.jetbrains.com/pycharm/) - Powerful IDE for Python

#### Shell

- [![Open-Source Software][oss icon]](https://github.com/fish-shell/fish-shell) [Fish](https://fishshell.com/) - A smart and user-friendly command-line shell.
- [![Open-Source Software][oss icon]](https://github.com/fisherman/fisherman) [Fisherman](https://github.com/fisherman/fisherman) - A plugin manager for fish shell.
- [![Open-Source Software][oss icon]](https://github.com/ipython/ipython) [Ipython](https://ipython.org/) - Powerful Python shell.
- [![Open-Source Software][oss icon]](https://github.com/oh-my-fish/oh-my-fish) [Oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) - Provides various packages and themes to extend the functionality of your fish shell.
- [![Open-Source Software][oss icon]](https://github.com/robbyrussell/oh-my-zsh) [Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) - A delightful community-driven framework for managing your zsh configuration.
- [![Open-Source Software][oss icon]](http://sourceforge.net/p/zsh/code/ci/master/tree/) [Zsh](http://www.zsh.org/) - A powerful command line shell.

#### Supporting Tools

- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/cscope/) [Cscope](http://cscope.sourceforge.net/) - Cscope is a developer's tool for browsing source code. Although cmd-line application, it is nativelly integrated with Vim editor. It allows searching code for symbols, definitions, functions (called/calling), regex, files.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/diffuse/files/?source=navbar) [Diffuse](https://sourceforge.net/projects/diffuse/) - Diffuse is a graphical tool for comparing and merging text files. It can retrieve files for comparison from Bazaar, CVS, Darcs, Git, Mercurial, Monotone, RCS, Subversion, and SVK repositories.
- [![Open-Source Software][oss icon]](https://www.fossil-scm.org/index.html/dir?ci=tip) [Fossil](https://www.fossil-scm.org) - Self-contained, distributed software configuration management system with integrated bug-tracking, wiki, technotes and web interface.
- [Genymotion](https://www.genymotion.com/features/) - Genymotion is a fast third-party emulator that can be used instead of the default Android emulator.
- [![Open-Source Software][oss icon]](https://git.gnome.org//browse/giggle/) [Giggle](https://wiki.gnome.org/action/show/Apps/giggle?action=show&redirect=giggle) - Giggle is a graphical frontend for the git content tracker.
- [![Open-Source Software][oss icon]](https://github.com/Gisto/Gisto) [Gisto](http://www.gistoapp.com/) - Gisto is a code snippet manager that runs on GitHub Gists and adds additional features such as searching, tagging and sharing gists while including a rich code editor.
- [![Open-Source Software][oss icon]](https://github.com/git/git) [Git](https://git-scm.com/) - Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [![Open-Source Software][oss icon]](https://github.com/git-cola/git-cola) [GitCola](http://git-cola.github.io/) - Git Cola is a sleek and powerful graphical Git client. Written in Python and GPL-licensed.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Gitg#Development_Resources) [Gitg](https://wiki.gnome.org/Apps/Gitg) - gitg is the GNOME GUI client to view git repositories.
- [GitKraken](https://www.gitkraken.com/) - The downright luxurious Git GUI client,for Windows, Mac & Linux.
- [Git](https://git-scm.com/) - Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [![Open-Source Software][oss icon]](https://github.com/gitlabhq/gitlabhq) [GitLab](https://github.com/gitlabhq/gitlabhq) - GitLab is a web-based Git repository manager with wiki and issue tracking features.
- [![Open-Source Software][oss icon]](https://github.com/sitaramc/gitolite) [Gitolite](http://gitolite.com/gitolite/index.html) - Gitolite allows you to setup git hosting on a central server, with fine-grained access control and many more powerful features.
- [Insomnia](https://insomnia.rest/) - A simple, beautiful, and free REST API client.
- [![Open-Source Software][oss icon]](https://jupyter.readthedocs.io/en/latest/install.html) [Jupyter Notebook](https://jupyter.org/) - An open source program that provides interactive data and scientific computing information across over 40 programming languages.
- [![Open-Source Software][oss icon]](http://meldmerge.org/development.html) [Meld](http://meldmerge.org/) - Meld is a visual diff and merge tool that helps you compare files, directories, and version controlled projects.
- [Mockingbot](https://mockingbot.in/?) - Mockingbot is an easy-to-use prototyping tool.
- [![Open-Source Software][oss icon]](https://github.com/evolus/pencil) [Pencil](http://pencil.evolus.vn/) - An open-source GUI prototyping tool that's available for ALL platforms.
- [![Open-Source Software][oss icon]](https://github.com/stuartlangridge/ColourPicker) [Pick](http://kryogenix.org/code/pick/) - Simple color picker.
- [Postman](https://www.getpostman.com) - Postman, allows a user to develop and test APIs quickly.
- [![Open-Source Software][oss icon]](https://github.com/rabbitvcs/rabbitvcs) [Rabbit VCS](http://rabbitvcs.org/) - RabbitVCS is a set of graphical tools written to provide simple and straightforward access to the version control systems you use.
- ![Nonfree][money icon] [SmartGit](http://www.syntevo.com/smartgit/) - SmartGit is a Git client with support for GitHub Pull Requests+Comments and SVN.
- ![Non Free][money icon] [StarUML](http://staruml.io/) - A sophisticated software modeler.
- [![Open-Source Software][oss icon]](http://uncrustify.sourceforge.net/) [Uncrustify](http://uncrustify.sourceforge.net/) - Source Code Beautifier for C, C++, C#, ObjectiveC, D, Java, Pawn and VALA. See UniversalIndentGUI below.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/universalindent/files/uigui/) [UniversalIndentGUI](http://universalindent.sourceforge.net/) - UniversalIndentGUI offers a live preview for setting the parameters of nearly any indenter.
- [![Open-Source Software][oss icon]](https://www.gnu.org/software/wdiff/devguide) [Wdiff](https://www.gnu.org/software/wdiff/) - The GNU wdiff program is a front end to diff for comparing files on a word per word basis. It collects the diff output and uses it to produce a nicer display of word differences between the original files.
- [![Open-Source Software][oss icon]](https://gitlab.com/wireshark/wireshark/-/tree/master) [Wireshark](https://www.wireshark.org/) - Wireshark is the world's foremost network protocol analyzer. It lets you see what's happening on your network at a microscopic level. It is the de facto (and often de jure) standard across many industries and educational institutions.
- [![Open-Source Software][oss icon]](https://github.com/zealdocs/zeal) [Zeal](https://zealdocs.org/) - Zeal is an offline documentation browser for software developers.

### E-Book Utilities

- [![Open-Source Software][oss icon]](https://github.com/babluboy/bookworm) [Bookworm](https://babluboy.github.io/bookworm/) - A simple, focused eBook reader.
- [![Open-Source Software][oss icon]](https://github.com/oguzhaninan/Buka) [Buka](https://github.com/oguzhaninan/Buka/releases) - A program for EBook Management.
- [![Open-Source Software][oss icon]](https://github.com/kovidgoyal/calibre) [Calibre](http://calibre-ebook.com/) - Incredibly ugly but powerful software for ebook management and conversion.
- [![Open-Source Software][oss icon]](https://github.com/janeczku/calibre-web) [Calibre-web](https://github.com/janeczku/calibre-web) - Calibre Web is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.
- [![Open-Source Software][oss icon]](https://github.com/michaldaniel/Ebook-Viewer) [Easy Ebook Viewer](https://github.com/michaldaniel/Ebook-Viewer) - Modern GTK Python Ebook Reader app to easily read epub files.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Evince/GettingEvince) [Evince](https://wiki.gnome.org/Apps/Evince) - Evince is a document viewer for multiple document formats. The goal of evince is to replace the multiple document viewers that exist on the GNOME Desktop with a single simple application.
- [![Open-Source Software][oss icon]](https://github.com/geometer/FBReader) [FBReader](https://fbreader.org/content/fbreader-beta-linux-desktop) - One of the most popular eReader apps.
- [Foxit](https://www.foxitsoftware.com/products/pdf-reader/) - Foxit Reader 8.0—Award-winning PDF Reader.
- [![Open-Source Software][oss icon]](https://github.com/martamilakovic/gnome-books) [Gnome Books](https://github.com/martamilakovic/gnome-books) - GNOME Books is application for listing, searching and reading eBooks.
- [![Open-Source Software][oss icon]](http://repo.or.cz/w/llpp.git) [llpp](https://wiki.archlinux.org/index.php/Llpp) - A lightweight, fast, customizable and featureful PDF, EPUB, XPS and CBZ viewer with vi-like keybindings based on MuPDF.
- [Lucidor](http://www.lucidor.org/lucidor/) - Lucidor is a computer program for reading and handling e-books. Lucidor supports e-books in the EPUB file format, and catalogs in the OPDS format.
- [MasterPDF editor](https://code-industry.net/free-pdf-editor/) - Master PDF Editor a convenient and smart PDF editor for Linux.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/mcomix/git/ci/master/tree/) [Mcomix](https://sourceforge.net/projects/mcomix/) - GTK+ comic book viewer.
- [![Open-Source Software][oss icon]](http://git.ghostscript.com/?p=mupdf.git;a=summary) [MuPDF](http://mupdf.com/) - a lightweight PDF and XPS viewer.
- [![Open-Source Software][oss icon]](https://github.com/KDE/okular) [Okular](https://okular.kde.org/) - Okular is a universal document viewer based developed by KDE. Okular works on multiple platforms, including but not limited to Linux, Windows, Mac OS X, BSD, etc.
- [![Open-Source Software][oss icon]](https://github.com/torakiki/pdfsam) [PDFsam](http://www.pdfsam.org/) - A desktop application to split, extract pages, rotate, mix and merge PDF files.
- [![Open-Source Software][oss icon]](https://download.kde.org/stable/peruse/peruse-1.2.tar.xz.mirrorlist) [Peruse](https://peruse.kde.org/) - A pleasant way to read comic books.
- [![Open-Source Software][oss icon]](https://launchpad.net/qpdfview) [qpdf](https://launchpad.net/qpdfview) - qpdfview is a tabbed document viewer.
- [![Open-Source Software][oss icon]](https://github.com/Sigil-Ebook/Sigil) [Sigil](https://github.com/Sigil-Ebook/Sigil) - Sigil is a multi-platform EPUB ebook editor.
- [![Open-Source Software][oss icon]](https://git.pwmt.org/pwmt/zathura.git) [Zathura](https://pwmt.org/projects/zathura/) - Zathura is a highly customizable and functional document viewer.

### Editors

- [![Open-Source Software][oss icon]](https://github.com/atom/atom) [Atom](https://atom.io/) - ซอฟต์แวร์แก้ไขข้อความ ที่สามารถปรับแต่งได้อย่างอิสระ สำหรับ ศตวรรษที่ 21
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/bluefish/code/HEAD/tree/trunk/bluefish/) [Bluefish](https://bluefish.openoffice.nl/index.html) - Bluefish คือซอฟต์แวร์แก้ไขข้อความสำหรับโปรแกรมเมอร์และนักพัฒนาเว็บไซต์ ที่มีประสิทธิภาพ
- [![Open-Source Software][oss icon]](https://github.com/adobe/brackets) [Brackets](https://brackets.io/) - ซอฟต์แวร์แก้ไขข้อความที่ทันสมัย และใช้ได้ดีสำหรับการออกแบบเว็บไซต์
- [![Open-Source Software][oss icon]](https://github.com/emacs-mirror/emacs) [Emacs](https://www.gnu.org/software/emacs/) - ซอฟต์แวร์แก้ไขข้อความ ที่ปรับแต่งได้อย่างอิสระ ฟรี และ อีกมากมาย
- [![Open-Source Software][oss icon]](https://www.geany.org/Download/Git) [Geany](https://www.geany.org/) - Geany คือซอฟต์แวร์แก้ไขข้อความที่ใช้ GTK+ ในการพัฒนา มาพร้อมกับฟีเจอร์พื้นฐาน, ขนาดเล็ก ทำงานได้รวดเร็ว โดยไม่ต้องติดตั้งส่วนอื่นเพิ่มเติม
- [![Open-Source Software][oss icon]](https://git.gnome.org//browse/gedit/) [Gedit](https://wiki.gnome.org/Apps/Gedit) - gedit คือซอฟต์แวร์แก้ไขข้อความจาก GNOME ซึ่งมุ่งเน้นให้ใช้งานได้ง่าย
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gnome-builder) [Gnome Builder](https://wiki.gnome.org/Apps/Builder) - ซอฟต์แวร์ IDE ประสิทธิภาพสูง สำหรับการพัฒนาด้วย C / C++ / Bash / JavaScript, สร้างโดยทีมจาก Gnome, เป็นหนึ่งใน IDE สำหรับการพัฒนาด้วยภาษา C/C++ ที่ดีที่สุด (รองรับในตัว Cmake)
- [![Open-Source Software][oss icon]](https://github.com/mawww/kakoune) [Kakoune](http://kakoune.org/) - Kakoune code editor - ซอฟต์แวร์ที่ได้แรงบันดาลใจจาก Vim, ใช้จำนวนการพิมพ์ที่น้อยกว่า สามารถเลือกข้อความได้หลายตำแหน่งพร้อมกัน
- [![Open-Source Software][oss icon]](https://kate-editor.org/build-it/) [Kate](https://kate-editor.org/get-it/) - Kate คือซอฟต์แวร์ที่เปิดได้หลายไฟล์พร้อมกัน และเป็นส่วนหนึ่งของ KDE ตั้งแต่รุ่น 2.2.
- [![Open-Source Software][oss icon]](https://github.com/Komodo/KomodoEdit) [Komodo Edit](https://github.com/Komodo/KomodoEdit) - ซอฟต์แวร์ฟรีและโอเพนซอร์ส สำหรับพัฒนาโปรแกรม รองรับหลายภาษา
- [![Open-Source Software][oss icon]](https://github.com/LightTable/LightTable) [Lighttable](http://lighttable.com/) - The next generation code editor! Support live coding.
- [![Open-Source Software][oss icon]](https://github.com/syl20bnr/spacemacs) [Spacemacs](http://spacemacs.org) - ชุดซอฟต์แวร์ Emacs ที่ร่วมกันพัฒนาโดยชุมชน
- [Sublime](https://www.sublimetext.com/) - ซอฟต์แวร์แก้ไขข้อความมากประสิทธิภาพ มีฟีเจอร์ค้นหาขั้นสูง และเพิ่มประสิทธิภาพด้านอื่นผ่านปลั๊กอิน
- [![Open-Source Software][oss icon]](https://github.com/orbitalquark/textadept) [Textadept](https://orbitalquark.github.io/textadept/) - Minimalist text editor for programmers. Textadept is extensible with Lua programming language.
- [![Open-Source Software][oss icon]](https://github.com/vim/vim) [Vim](http://www.vim.org/download.php) - Vim คือซอฟต์แวร์แก้ไขข้อความขั้นสูง ซึ่งมุ่งไปที่การให้ประสิทธิภาพเช่นเดียวกับ ซอฟต์แวร์ 'Vi' ที่ใช้แพร่หลายใน Unix แต่มีฟีเจอร์ที่ครบครันกว่า เหมาะสำหรับผู้ที่ใช้ vi เป็นปกติอยู่แล้ว
- [![Open-Source Software][oss icon]](https://github.com/Microsoft/vscode) [VSCode](https://code.visualstudio.com) - Visual Studio Code คือซอฟต์แวร์แก้ไขโค้ดขนาดเล็ก แต่มีประสิทธิภาพ ซึ่งสามารถใช้บนเดสก์ท็อปได้ ทั้ง Windows, OS X และ Linux, ตัวซอฟต์แวร์รองรับ JavaScript, TypeScript และ Node.js ในตัว และยังสามารถรองรับภาษาอื่นๆ ได้ (C++, C#, Python, PHP, Golang)
- [![Open-Source Software][oss icon]](http://git.savannah.gnu.org/cgit/nano.git/) [Nano](https://www.nano-editor.org/) - GNU Nano คือซอฟต์แวร์แก้ไขข้อความอย่างง่าย ที่ใช้งานบนคอนโซลได้ง่าย
- [![Open-Source Software][oss icon]](https://github.com/neovim/neovim) [Neovim](https://neovim.io/) - Neovim คือซอฟต์แวร์ที่ fork จาก Vim ซึ่งมุ่งเน้นในการให้ประสบการณ์ที่ดีต่อผู้ใช้ และ ปลั๊กอิน
- [![Open-Source Software][oss icon]](https://github.com/zyedidia/micro) [Micro](https://micro-editor.github.io/) - Micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.

### Education

- [![Open-Source Software][oss icon]](https://apps.ankiweb.net/) [Anki](https://apps.ankiweb.net/) - Powerful, intelligent flash cards which makes remembering things easy.
- [![Open-Source Software][oss icon]](http://artha.sourceforge.net/wiki/index.php/Download#Source) [Artha](http://artha.sourceforge.net/wiki/index.php/Home) - Artha is a free cross-platform English thesaurus that works completely off-line and is based on WordNet.
- [![Open-Source Software][oss icon]](https://github.com/bibletime/bibletime) [BibleTime](http://bibletime.info/) - BibleTime is a Bible study application based on the Sword library and Qt toolkit.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/celestia/files/Celestia-source/1.6.1/celestia-1.6.1.tar.gz/download) [Celestia](http://celestiaproject.net/) - The free space simulation that lets you explore our universe in three dimensions.
- [![Open-Source Software][oss icon]](https://github.com/opp11/chemtool/blob/master/README.md) [Chemtool](http://ruby.chemie.uni-freiburg.de/~martin/chemtool/) - Chemtool is a small program for drawing chemical structures on Linux.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/epoptes) [Epoptes](http://www.epoptes.org/) - An open source computer lab management and monitoring tool.
- [![Open-Source Software][oss icon]](https://github.com/gap-system/gap) [GAP](http://www.gap-system.org/) - A computer algebra system for computational discrete algebra with particular emphasis on computational group theory.
- [![Open-Source Software][oss icon]](http://gcompris.net/wiki/Developer%27s_corner) [Gcompris](http://gcompris.net/index-en.html) - GCompris is a high quality educational software suite comprising of numerous activities for children aged 2 to 10.
- [![Open-Source Software][oss icon]](https://github.com/geogebra/geogebra) [Geogebra](https://www.geogebra.org/download) - The graphing calculator for functions, geometry, algebra, calculus, statistics and 3D mathematics.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Dictionary) [Gnome-dictionary](https://wiki.gnome.org/Apps/Dictionary) - A powerful dictionary for GNOME.
- [![Open-Source Software][oss icon]](http://opensis.sourceforge.net/) [GNU Octave](http://www.gnu.org/software/octave/) - GNU Octave is a scientific programming language, primarily intended for numerical computations, that is mostly compatible with MATLAB.
- [![Open-Source Software][oss icon]](http://ftp.gnu.org/gnu/gtypist/) [GNU Typist](https://www.gnu.org/software/gtypist/index.html) - ncurses-based free-software typing instructor
- [![Open-Source Software][oss icon]](https://gitlab.com/gnukhata) [GNUKhata](http://www.gnukhata.in/) - Open source accounting software.
- [Google Earth](https://itsfoss.com/install-google-earth-ubunu/) - Google Earth is a virtual globe, map and geographical information program.
- [![Open-Source Software][oss icon]](http://gperiodic.seul.org/cvs/) [GPeriodic](http://gperiodic.seul.org/) - GPeriodic is a periodic table application for Linux.
- [KDE Edu Suite](https://edu.kde.org/) - Free Educational Software based on the KDE technologies.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/klavaro) [Klavaro](http://klavaro.sourceforge.net/en/index.html) - A touch typing tutor very flexible, supporting customizable keyboard layouts. You can edit and save new or unknown keyboard layouts, as the basic course was designed to not depend on specific ones. Also, there are some charts about the learning process.
- [![Open-Source Software][oss icon]](https://github.com/KDE/ktouch) [Ktouch](https://github.com/KDE/ktouch) - KTouch is a program to learn and practice touch typing.
- ![Nonfree][money icon] [MAPLE](http://www.maplesoft.com/products/maple/) - Maple is math software that combines the world's most powerful math engine with an interface that makes it extremely easy to analyze, explore, visualize, and solve mathematical problems.
- ![Nonfree][money icon] [MapTiler](https://www.maptiler.com/) - MapTiler generates zoomable raster maps from images in user-defined coordinate system.
- [![Open-Source Software][oss icon]](https://github.com/KDE/marble) [Marble](https://marble.kde.org/) - Marble is a virtual globe and world atlas — your swiss army knife for maps.
- ![Nonfree][money icon] [MATLAB](http://www.mathworks.com/products/matlab/?requestedDomain=www.mathworks.com) - The MATLAB platform is optimized for solving engineering and scientific problems. MATLAB helps you take your ideas beyond the desktop. You can run your analyses on larger data sets and scale up to clusters and clouds.![Nonfree][money icon]
- [![Open-Source Software][oss icon]](http://maxima.sourceforge.net/project.html) [Maxima](http://maxima.sourceforge.net/) - Maxima is a system for the manipulation of symbolic and numerical expressions, including differentiation, integration, Taylor series, Laplace transforms, ordinary differential equations, systems of linear equations, and much more.
- [Mendeley](https://www.mendeley.com/) - Mendeley is a program for managing and sharing research papers, finding research data and collaborating online.
- [![Open-Source Software][oss icon]](https://github.com/moodle/moodle) [Moodle](https://download.moodle.org/) - Course management system for online learning.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/openeuclide/) [OpenEuclid](http://coulon.publi.free.fr/openeuclide/) - OpenEuclide is a 2D geometry software: figures are defined dynamically by describing formal geometrical constraints.
- [![Open-Source Software][oss icon]](https://github.com/openmaptiles) [OpenMapTiles](https://openmaptiles.org/) - OpenMapTiles is a set of open-source tools for self-hosting of OpenStreetMaps in more than 50 languages. It provides both raster as well as vector tiles, WMS, WMTS, support for JavaScript viewers and mobile SDK.
- [![Open-Source Software][oss icon]](http://opensis.sourceforge.net/) [OpenSIS](http://www.opensis.com/home) - School Management Software that Increases Student Achievements & Teacher Performances.
- [![Open-Source Software][oss icon]](http://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi?p=pari.git;a=summary) [PARI/GP](http://pari.math.u-bordeaux.fr/) - A computer algebra system for fast computations in number theory.
- [![Open-Source Software][oss icon]](https://git.sagemath.org/sage.git/) [SageMath](http://www.sagemath.org/) - A mathematical software with features covering many aspects of mathematics, including algebra, combinatorics, numerical mathematics, number theory, and calculus.
- [![Open-Source Software][oss icon]](https://github.com/scipy/scipy) [Scipy](https://scipy.org/install.html) - SciPy is a Python-based ecosystem of open-source software for mathematics, science, and engineering.
- [![Open-Source Software][oss icon]](https://github.com/LLK/scratch-flash) [Scratch](https://scratch.mit.edu/) - With Scratch, you can program your own interactive stories, games, and animations — and share your creations with others in the online community.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/stellarium/code/HEAD/tree/) [Stellarium](http://www.stellarium.org/) - Stellarium is a free open source planetarium for your computer.
- [![Open-Source Software][oss icon]](https://github.com/ugeneunipro/ugene) [UGENE](http://ugene.net/) - UGENE is free open-source cross-platform integrated GUI-based bioinformatics software.
- [![Open-Source Software][oss icon]](https://github.com/veyon/veyon) [Veyon](https://github.com/veyon/veyon/releases) - Veyon is a computer management software for classrooms, it allows a teacher to control student computers and guide students over a computer network.

### Email

- [![Open-Source Software][oss icon]](http://git.claws-mail.org/) [Claws](http://www.claws-mail.org/) - Claws is an email client and news reader, featuring sophisticated interface, easy configuration, intuitive operation, abundant features and plugins, robustness and stability.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Evolution/#Get_the_Source_Code) [Evolution](https://wiki.gnome.org/Apps/Evolution/) - Evolution is a personal information management application that provides integrated mail, calendaring and address book functionality.
- [![Open-Source Software][oss icon]](https://git.gnome.org//browse/geary/) [Geary](https://wiki.gnome.org/Apps/Geary) - Geary is an email application built for GNOME 3. It allows you to read and send email with a simple, modern interface.
- [Hiri](https://www.hiri.com/) - Hiri is a business focused desktop e-mail client for sending and receiving e-mails, managing calendars, contacts, and tasks.
- [![Open-Source Software][oss icon]](https://cgit.kde.org/kmail.git/) [KMail](https://apps.kde.org/de/kmail2/) - KMail is the email component of Kontact, the integrated personal information manager from KDE.
- [![Open-Source Software][oss icon]](https://github.com/pulb/mailnag) [Mailnag](https://launchpad.net/~pulb/+archive/ubuntu/mailnag) - Mailnag is a daemon program that checks POP3 and IMAP servers for new mail.
- [Mailspring](https://getmailspring.com/) - A beautiful, fast and maintained fork of Nylas Mail by one of the original authors.
- [![Open-Source Software][oss icon]](http://sylpheed.sraoss.jp/en/download.html#stable) [Sylpheed](http://sylpheed.sraoss.jp/en/) - Lightweight and user-friendly e-mail client.
- [![Open-Source Software][oss icon]](https://releases.mozilla.org/pub/thunderbird/) [Thunderbird](https://www.mozilla.org/en-US/thunderbird/) - Thunderbird is a free email application that’s easy to set up and customize and it’s loaded with great features.
- [![Open-Source Software][oss icon]](https://github.com/KDE/trojita) [Trojita](https://apps.kde.org/trojita/) - A super fast desktop email client for Linux.
- [![Open-Source Software][oss icon]](https://github.com/danchoi/vmail) [Vmail](http://danielchoi.com/software/vmail.html) - Vim-like Gmail client.
- [![Open-Source Software][oss icon]](https://github.com/Thomas101/wmail) [Wmail](https://github.com/Thomas101/wmail) - Gmail & Google Inbox unofficial desktop client for linux.

### File Manager

- [![Open-Source Software][oss icon]](https://github.com/pornel/7z) [7Zip](http://www.7-zip.org/download.html) - ซอฟต์แวร์ที่สามารถจัดการไฟล์บีบอัดได้เกือบทุกฟอร์แมต
- [![Open-Source Software][oss icon]](https://github.com/mate-desktop/caja) [Caja](https://mate-desktop.org/) - Is the default file manager for the MATE desktop environment, it is very fast and simple to use.
- [![Open-Source Software][oss icon]](https://github.com/KDE/dolphin) [Dolphin](https://userbase.kde.org/Dolphin) - Dolphin is the default file manager of the KDE desktop environment featuring usability as well as functionality.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/doublecmd/) [Double Commander](http://doublecmd.sourceforge.net/) - Double Commander is a cross platform open source file manager with two panels side by side. It is inspired by Total Commander and features some new ideas.
- [![Open-Source Software][oss icon]](https://krusader.org/get-involved/index.html) [Krusader](https://krusader.org) - Krusader is an advanced twin panel (commander style) file manager for KDE and other desktops in the \*nix world, similar to Midnight or Total Commander.
- [![Open-Source Software][oss icon]](https://github.com/MidnightCommander) [Midnight Commander](https://www.midnight-commander.org/) - A feature rich full-screen file manager that allows you to copy, move and delete files and whole directory trees.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/nautilus) [Nautilus](https://wiki.gnome.org/Apps/Nautilus) - Nautilus (Files) is a file manager designed to fit the Gnome desktop design and behaviour, giving the user a simple way to navigate and manage its files.
- [![Open-Source Software][oss icon]](https://github.com/linuxmint/nemo) [Nemo](http://askubuntu.com/questions/294421/how-do-i-install-nemo-file-manager) - Nemo is the file manager for the Cinnamon desktop environment.
- [![Open-Source Software][oss icon]](https://github.com/jarun/nnn) [nnn](https://github.com/jarun/nnn) - A very lightweight and fast terminal file browser with excellent desktop integration.
- [![Open-Source Software][oss icon]](https://github.com/teejee2008/polo) [Polo](https://github.com/teejee2008/polo) - Polo is a modern, light-weight file manager for Linux with support for multiple panes and tabs; support for archives, and much more.
- [![Open-Source Software][oss icon]](https://github.com/shundhammer/qdirstat) [QDirStat](https://github.com/shundhammer/qdirstat#ubuntu) - Qt-based directory statistics - KDirStat without any KDE, from the original KDirStat author.
- [![Open-Source Software][oss icon]](https://github.com/ranger/ranger) [Ranger](http://ranger.nongnu.org/) - Ranger is a console file manager with VI key bindings.
- [![Open-Source Software][oss icon]](https://github.com/luisgg/thunar) [Thunar](https://apps.ubuntu.com/cat/applications/precise/thunar/) - Thunar is the file manager designed to be the default file manager of Xfce 4.6 It has been designed to be fast and easy to use.
- [![Open-Source Software][oss icon]](https://github.com/vifm/vifm) [Vifm](https://vifm.info/) - Vifm is an ncurses based file manager with VI like keybindings, which also borrows some useful ideas from mutt.

### Games

#### City Building Simulation

- [Dwarf Fortress](http://www.bay12games.com/dwarves/) - A famously complex simulation of a High Fantasy Dwarf Fortress, fight goblins, and slay massive legendary beasts. Strike the earth!
- [![Open-Source Software][oss icon]](https://github.com/OpenTTD/OpenTTD) [OpenTTD](https://www.openttd.org/) - An open-source clone of Transport Tycoon Plus with major improvements.
- [![Open-Source Software][oss icon]](https://github.com/aburch/simutrans) [Simutrans](https://www.simutrans.com) - Simutrans is a freeware and open-source transportation simulator.
- [![Open-Source Software][oss icon]](https://github.com/unknown-horizons/unknown-horizons) [Unknown Horizons](http://unknown-horizons.org/) - A 2D realtime strategy simulation with an emphasis on economy and city building. Multiplayer currently broken.

#### Command Line Games

- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [2048](https://itsfoss.com/best-command-line-games-linux/) - Play the famous 2048 in commandline.
- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [Backgammon](https://itsfoss.com/best-command-line-games-linux/) - Play Backgammon in commandline.
- [![Open-Source Software][oss icon]](https://github.com/fph/bastet) [Bastet](https://github.com/fph/bastet) - Play Tetris in commandline.
- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [Greed](https://itsfoss.com/best-command-line-games-linux/) - Tron game in the linux command line.
- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [Ninvaders](https://itsfoss.com/best-command-line-games-linux/) - Play Space Invaders on the command line.
- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [nSnake](https://itsfoss.com/best-command-line-games-linux/) - Play the classic Nokia snake game on the command line.
- [![Open-Source Software][oss icon]](https://github.com/alexdantas/pacman4console.debian) [Pacman4console](https://launchpad.net/ubuntu/+source/pacman4console) - Play Pacman game in console.
- [![Open-Source Software][oss icon]](https://itsfoss.com/best-command-line-games-linux/) [Tron](https://itsfoss.com/best-command-line-games-linux/) - Play the best action game, Tron in the command line.

#### Engine Re-creations (require the actual game)

- ![Open-Source Software][oss icon] [NXEngine](http://nxengine.sourceforge.net/) - A source port of Cave Story that runs natively on Linux, source needs to be built.
- [![Open-Source Software][oss icon]](https://github.com/SFTtech/openage) [openage](http://openage.sft.mx/) - Free (as in freedom) open source clone of the Age of Empires II engine, source needs to be built.
- [![Open-Source Software][oss icon]](https://github.com/OpenMW/openmw) [OpenMW](http://openmw.org) - A recreation of the Morrowind engine, expanding upon the original. It can be used to play legitimate copies of original game.
- [![Open-Source Software][oss icon]](https://github.com/OpenRA/OpenRA) [OpenRA](http://www.openra.net/) - Classic strategy games, rebuilt for the modern era. Open source.
- [![Open-Source Software][oss icon]](https://github.com/OpenRCT2/OpenRCT2) [OpenRCT2](https://openrct2.website/) - A recreation of the Rollercoaster Tycoon 2 engine. Requires the original games assests.

#### FPS

- [![Open-Source Software][oss icon]](https://gitlab.com/groups/xonotic) [ChaosEsqueAnthology Disc 1](https://sourceforge.net/projects/chaosesqueanthology/) [ChaosEsqueAnthology Disc 2](https://sourceforge.net/projects/chaosesqueanthologyvolume2/) - A modification of Xonotic which included extended weapons, maps, vehicles, buildable buildings, mounted weapons, spell casting, monsters, player characters, textures, and game mode (such as colorwar (think liquidwar))
- [![Open-Source Software][oss icon]](https://github.com/freedoom/freedoom) [Freedoom](https://freedoom.github.io/) - The Freedoom project aims to create a complete free content game based on the Doom engine.
- [![Open-Source Software][oss icon]](https://github.com/red-eclipse/base) [Red Eclipse](https://redeclipse.net/) - Red Eclipse is a fun-filled new take on the first person arena shooter, which lends itself toward a balanced gameplay, with a general theme of agility in a variety of environments.
- ![Open-Source Software][oss icon] [Urban Terror](http://www.urbanterror.info) - A "Hollywood" tactical shooter - realism based, but the motto is "fun over realism".
- [![Open-Source Software][oss icon]](https://gitlab.com/groups/xonotic) [Xonotic](http://www.xonotic.org/) - Arena shooter inspired by Unreal Tournament and Quake.
- [![Open-Source Software][oss icon]](https://osdn.net/projects/zandronum/scm/) [Zandronum](http://zandronum.com/) - Leading the way in newschool multiplayer Doom online.
- [![Open-Source Software][oss icon]](https://github.com/coelckers/gzdoom) [Zdoom](https://zdoom.org/index) - ZDoom is a source port for the modern era, supporting current hardware and operating systems and sporting a vast array of user options.

#### Gaming Applications

- [![Open-Source Software][oss icon]](https://github.com/itchio/itch) [itch](https://itch.io/) - The itch.io app. All of your downloads are kept in a single place and are automatically updated. Plenty of free games.
- [![Open-Source Software][oss icon]](https://github.com/lutris/lutris) [Lutris](https://lutris.net/) - Lutris is an open gaming platform for Linux. It helps you install and manage your games in a unified interface.
- [![Open-Source Software][oss icon]](http://repository.playonlinux.com/) [PlayOnLinux](https://www.playonlinux.com) - A front-end for Wine.
- [![Open-Source Software][oss icon]](https://github.com/libretro/RetroArch) [RetroArch](http://www.retroarch.com/) - A front-end for a lot of game emulators.
- [Steam](steampowered.com) - Gaming store, which opens the gates to many games.
- [![Open-Source Software][oss icon]](https://dl.winehq.org/wine/source/) [Wine](https://www.winehq.org/) - Wine ("Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on Linux, quality depends from game to game.

#### Machine emulators

- [![Open-Source Software][oss icon]](https://github.com/dolphin-emu/dolphin) [Dolphin Emulator](https://dolphin-emu.org/) - Dolphin is a GameCube / Wii emulator, allowing you to play games for these two platforms on PC with improvements.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/fuse-emulator/fuse/ci/master/tree/) [Fuse](http://fuse-emulator.sourceforge.net/) - Fuse (the Free Unix Spectrum Emulator) is a ZX Spectrum emulator for Unix.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gnome-video-arcade) [GNOME Video Arcade](https://wiki.gnome.org/action/show/Apps/GnomeVideoArcade?action=show&redirect=GnomeVideoArcade) - GNOME Video Arcade is a simple Mame frontend for any freedesktop.org compliant desktop environment.
- [![Open-Source Software][oss icon]](https://github.com/mamedev/mame) [MAME](http://mamedev.org/) - MAME is an Arcade Cabinet emulator that strives for accuracy, and can play a huge number of different arcade games.
- [![Open-Source Software][oss icon]](https://github.com/0ldsk00l/nestopia) [nestopia](http://0ldsk00l.ca/nestopia/) - nestopia is a Nintendo Entertainment System/Famicon emulator.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/qmc2/files/qmc2/) [qmc2](https://qmc2.batcom-it.net/) - QMC2 is the successor to QMamecat, it is a gui for MAME and a ROM manager.
- [![Open-Source Software][oss icon]](https://github.com/snes9xgit/snes9x) [Snes9x](http://www.snes9x.com/) - Is a multiplatform Super Nintendo Entertainment System emulator that has gone through many incarnations, but is still being actively developed.
- [![Open-Source Software][oss icon]](https://github.com/stella-emu/stella) [Stella](https://stella-emu.github.io/) - is an Atari 2600 Emulator that is multiplatform.
- [![Open-Source Software][oss icon]](https://github.com/visualboyadvance-m/visualboyadvance-m) [Visual Boy Advance-M](http://vba-m.com/) - A Gameboy and Gameboy Advance Emulator that is still undergoing active development and can even emulate a system link between two gameboys.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/zsnes/files/zsnes/ZSNES%20v1.51/) [ZSNES](http://www.zsnes.com/) - A capable and commonly used Super Nintendo Entertainment System/Super Famicom emulator, many consider it the gold standard in SNES/Super Famicom emulation.

#### Miscellaneous

- ![Open-Source Software][oss icon] [Cockatrice](https://cockatrice.github.io/) - Cockatrice is an open-source multiplatform supported program for playing tabletop card games over a network.
- [![Open-Source Software][oss icon]](https://download.savannah.gnu.org/releases/galois/source/) [Galois](http://www.nongnu.org/galois/) - Galois is a Falling Blocks type game that isn't limited to the standard tetrominoes that most games in it's genre are limited to.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/action/show/Apps/gbrainy?action=show&redirect=gbrainy#Source_code) [GBrainy](https://wiki.gnome.org/action/show/Apps/gbrainy?action=show&redirect=gbrainy) - Gbrainy is a brain teaser game with logic puzzles and memory trainers.
- ![Nonfree][money icon] [Minecraft](https://minecraft.net) - Minecraft is a game about placing blocks and going on adventures. Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles.
- [![Open-Source Software][oss icon]](https://github.com/minetest/minetest/) [Minetest](https://minetest.net) - Open-source Minecraft written in C++ (uses less resources) and includes modding API.
- ![Open-Source Software][oss icon] [Mudlet](mudlet.org) - A cross-platform, open source, and super fast MUD (text-only MMORPGs) client with scripting in Lua.
- [OhMyGiraffe](https://ohmygiraffe.com) - A delightful game of survival. A game about a giraffe eating fruit while being chased by lions.
- [![Open-Source Software][oss icon]](https://github.com/alpcoskun/snake) [Snake Game](https://alpcoskun.com/snake/) - Cross-platform Classic Snake Game based on Node.js.
- [![Open-Source Software][oss icon]](https://github.com/supertuxkart/stk-code) [SuperTuxKart](https://supertuxkart.net) - SuperTuxKart is a 3D open-source arcade racer with a variety characters, tracks, and modes to play.

#### RPG

- ![Open-Source Software][oss icon] [Tales of Maj'Eyal](https://te4.org/) - Tales of Maj’Eyal (ToME) is a free, open source roguelike RPG, featuring tactical turn-based combat and advanced character building.
- ![Open-Source Software][oss icon] [Zelda Classic](http://www.zeldaclassic.com/) - A tribute to Nintendo's The Legend of Zelda with additional quests, items and challenges.
- ![Open-Source Software][oss icon] [Zelda: Mystery of Solarus DX](http://www.solarus-games.org) - A direct sequel to The Legend of Zelda: A Link to the Past on the SNES, using the same graphics and game mechanisms.

#### RTS

- [![Open-Source Software][oss icon]](http://releases.wildfiregames.com/) [0 AD](https://play0ad.com/) - Age of Empires like RTS game of ancient warfare.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/nethack/NetHack/ci/NetHack-3.6.0/tree/) [Nethack](https://www.nethack.org/) - Open-source rogue-like with ASCII graphics.
- [![Open-Source Software][oss icon]](https://github.com/triplea-game/triplea/) [TripleA](http://www.triplea-game.org/) - Open source grand strategy game with "Axis and Allies" game rules.
- [![Open-Source Software][oss icon]](https://github.com/Warzone2100/warzone2100) [Warzone 2100](https://www.wz2100.net/) - Open-source real-time strategy game that takes place after a nuclear war.
- [![Open-Source Software][oss icon]](https://bazaar.launchpad.net/~widelands-dev/widelands/trunk/changes) [Widelands](https://wl.widelands.org/) - Widelands is a open source RTS game with singleplayer campaigns and a multiplayer mode inspired by Settlers II.

#### Turn Based Strategy

- [![Open-Source Software][oss icon]](https://github.com/wesnoth/wesnoth) [Battle for Wesnoth](https://wesnoth.org/) - The Battle for Wesnoth is an open source, turn-based strategy game with a high fantasy theme. It features both singleplayer and online/hotseat multiplayer combat.
- [![Open-Source Software][oss icon]](https://github.com/freeciv/freeciv) [FreeCiv](http://www.freeciv.org/) - Freeciv is a Free and Open Source empire-building strategy game inspired by the history of human civilization.

### Graphics

#### Graphic Creation

- [![Open-Source Software][oss icon]](https://github.com/aseprite/aseprite/) [Aseprite](https://www.aseprite.org/) - Animated sprite editor & pixel art tool.
- [![Open-Source Software][oss icon]](http://archive.blender.org/download/source-code/index.html) [Blender](https://www.blender.org/) - a free and open source complete 3D creation pipeline for artists and small teams.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/cinepaint/) [Cinepaint](http://cinepaint.org/) - Open source deep paint software.
- [![Open-Source Software][oss icon]](https://github.com/lettier/gifcurry) [Gifcurry](https://lettier.github.io/gifcurry/) - Your open source video to GIF maker built with Haskell.
- [Gravit](https://www.designer.io/) - Gravit Designer is a full featured free vector design app right at your fingertip.
- [Heron Animation](https://heronanimation.brunolefevre.net/) - A free stop animation making program.
- [![Open-Source Software][oss icon]](https://github.com/inkscape/inkscape) [Inkscape](https://inkscape.org/en/) - A powerful, free design tool for you , whether you are an illustrator, designer, web designer or just someone who needs to create some vector imagery.
- [![Open-Source Software][oss icon]](https://www.kde.org/applications/graphics/karbon/development) [Karbon](https://www.calligra.org/karbon/) - An open source vector drawing program.
- [![Open-Source Software][oss icon]](https://github.com/mbasaglia/Knotter) [Knotter](https://knotter.mattbas.org/Knotter) - A Program designed solely to help design and create Celtic Knots.
- [![Open-Source Software][oss icon]](https://github.com/KDE/krita) [Krita](https://krita.org/en/) - Open Source Software for Concept Artists, Digital Painters, and Illustrators.
- [![Open-Source Software][oss icon]](https://github.com/mypaint/mypaint/releases) [Mypaint](http://mypaint.org/about/) - Mypaint is a paint program for use with graphics tablets.
- [![Open-Source Software][oss icon]](https://github.com/jonata/opendvdproducer) [Open DVD Producer](http://opendvdproducer.jonata.org/) - A modern, open source cross platform software to produce DVD images.
- [![Open-Source Software][oss icon]](https://github.com/PintaProject/Pinta) [Pinta](https://pinta-project.com/pintaproject/pinta/) - Pinta is a free, open source program for drawing and image editing.
- [![Open-Source Software][oss icon]](https://launchpad.net/lsm) [StopMotion](http://linuxstopmotion.org/) - Linux Stopmotion is a Free Open Source application to create stop-motion animations. It helps you capture and edit the frames of your animation and export them as a single file.
- [![Open-Source Software][oss icon]](https://github.com/synfig/synfig) [Synfig Studio](http://www.synfig.org/) - Open-source 2D animation software.
- [![Open-Source Software][oss icon]](http://www.xaraxtreme.org/Developers/develeopers-source-code-a-building.html) [Xara Extreme](http://www.xaraxtreme.org/) - Xara Xtreme for Linux is a powerful, general purpose graphics program for Unix platforms including Linux, FreeBSD.
- [yEd Graph Editor](https://www.yworks.com/products/yed) - yEd is a powerful desktop application that can be used to quickly and effectively generate high-quality diagrams. Create diagrams manually, or import your external data for analysis. Our automatic layout algorithms arrange even large data sets with just the press of a button.
- [Vectr](https://vectr.com/) - Vectr is a free graphics software used to create vector graphics easily and intuitively. It's a simple yet powerful web and desktop cross-platform tool to bring your designs into reality.

#### Image Editor

- ![Nonfree][money icon] [Aftershot](http://www.aftershotpro.com/en/products/aftershot/pro/) - A powerful alternative to Adobe Photoshop.
- [![Open-Source Software][oss icon]](https://github.com/darktable-org/darktable) [Darktable](http://www.darktable.org/) - Darktable is an open source photography workflow application and RAW developer.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gimp) [GIMP](https://www.gimp.org/downloads/) - GIMP is a freely distributed program for such tasks as photo retouching, image composition and image authoring.
- [![Open-Source Software][oss icon]](http://www.graphicsmagick.org/) [GraphicsMagick](http://www.graphicsmagick.org/) - GraphicsMagick is the swiss army knife of image processing.
- [![Open-Source Software][oss icon]](http://hugin.sourceforge.net/) [Hugin](http://hugin.sourceforge.net/) - an easy to use cross-platform panoramic imaging toolchain based on Panorama Tools.
- [![Open-Source Software][oss icon]](https://github.com/ImageMagick/ImageMagick) [ImageMagik](http://www.imagemagick.org/script/index.php) - ImageMagick is a suite of command-line utilities for modifying and working with images.
- [![Open-Source Software][oss icon]](https://github.com/jarun/imgp) [imgp](https://github.com/jarun/imgp) - Blazing fast terminal image resizer and rotator.
- [![Open-Source Software][oss icon]](https://github.com/LuminanceHDR/LuminanceHDR) [Luminance HDR](https://sourceforge.net/projects/qtpfsgui/) - Luminance HDR is an open source graphical user interface application that aims to provide a workflow for HDR imaging.
- [![Open-Source Software][oss icon]](https://github.com/google-code-export/photivo) [Photivo](http://photivo.org/) - Photivo is a free and open source (GPL3) photo processor, handles your RAW and bitmap files (TIFF, JPEG, BMP, PNG and many more) in a non-destructive 16 bit processing pipe with gimp workflow integration and batch mode. It is intended to be used in a workflow together with digiKam/F-Spot/Shotwell and Gimp.
- [![Open-Source Software][oss icon]](https://github.com/piskelapp/piskel) [Piskel](https://www.piskelapp.com/) - Browser-based editor for animated sprites and pixel art. Available as offline application.
- [![Open-Source Software][oss icon]](https://github.com/lbalazscs/Pixelitor) [Pixelitor](http://pixelitor.sourceforge.net/) - Pixelitor is a free and open source image editing software that supports layers, layer masks, text layers, filters, multiple undo etc.
- [![Open-Source Software][oss icon]](https://github.com/Beep6581/RawTherapee) [RawTherapee](http://rawtherapee.com/) - A good looking but lesser known photo editing app.

#### Image Management

- [![Open-Source Software][oss icon]](https://github.com/KDE/digikam) [Digikam](http://www.digikam.org/) - DigiKam คือซอฟต์แวร์สำหรับจัดการรูปถ่ายขั้นสูงในลินุกซ์
- [![Open-Source Software][oss icon]](http://git.finalrewind.org/feh) [Feh](https://feh.finalrewind.org/) - lightweight and fast image viewer.
- [![Open-Source Software][oss icon]](http://www.kornelix.net/downloads/downloads.html) [Fotoxx](http://www.kornelix.net/fotoxx/fotoxx.html) - Fotoxx is a free open source Linux program for image editing and collection management.
- [![Open-Source Software][oss icon]](https://git.gnome.org/browse/gthumb/) [gThumb](https://wiki.gnome.org/Apps/gthumb) - gThumb is an image viewer and browser (it also includes an importer tool for transferring photos from cameras).
- [![Open-Source Software][oss icon]](https://cgit.kde.org/gwenview.git/tree//?) [gwenview](https://userbase.kde.org/Gwenview) - Simple yet powerful image viewer and management for KDE desktops.
- [![Open-Source Software][oss icon]](https://github.com/meowtec/Imagine) [Imagine](https://github.com/meowtec/Imagine) - An open source image optimizer that can shrink the size of images with a minimal loss of quality.
- [![Open-Source Software][oss icon]](https://github.com/nomacs/nomacs/tree/master) [nomacs](https://nomacs.org/) - nomacs is an image viewer that is able to view nearly any image format, and has powerful renaming and sorting tools.
- [![Open-Source Software][oss icon]](https://github.com/peterlevi/ojo) [Ojo](https://github.com/peterlevi/ojo) - A fast and pretty image viewer.
- [![Open-Source Software][oss icon]](https://github.com/ivandokov/phockup) [Phockup](https://github.com/ivandokov/phockup) - Command line sorting tool to organize photos and videos from your camera in folders by year, month and day.
- [![Open-Source Software][oss icon]](https://github.com/oferkv/phototonic) [Photonic](https://github.com/oferkv/phototonic) - Phototonic is image viewer and organizer.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Shotwell) [Shotwell](https://wiki.gnome.org/Apps/Shotwell) - Shotwell is a photo manager for GNOME 3.

#### Miscellaneous

- [![Open-Source Software][oss icon]](https://github.com/HandBrake/HandBrake) [Handbrake](https://handbrake.fr/) - HandBrake is a tool for converting video from nearly any format to a selection of modern, widely supported codecs.
- [![Open-Source Software][oss icon]](http://potrace.sourceforge.net/#downloading) [Potrace](http://potrace.sourceforge.net/) - Potrace is a tool for tracing a bitmap, which means, transforming a bitmap into a smooth, scalable image.
- [![Open-Source Software][oss icon]](https://www.radiance-online.org/download-install/radiance-source-code) [Radiance](http://www.radiance-online.org/) - Radiance - A Validated Lighting Simulation Tool.
- [![Open-Source Software][oss icon]](https://github.com/terkelg/ramme) [Ramme](https://github.com/terkelg/ramme) - Unofficial Instagram desktop application.
- [![Open-Source Software][oss icon]](https://launchpad.net/rapid/pyqt/0.9.0b2) [Rapid Photo Downloader](http://damonlynch.net/rapid/download.html) - Rapid Photo Downloader makes it easy to import photos from a camera or smartphone.

#### PSD, Sketch Inspection

- ![Nonfree][money icon] [Avocode](https://avocode.com/) - Avocode - Share and inspect Photoshop and Sketch designs in a heart beat.

#### Screen Recorder

- [![Open-Source Software][oss icon]](https://github.com/asciinema/asciinema) [asciinema](https://asciinema.org) - Terminal session recorder.
- [![Open-Source Software][oss icon]](https://github.com/foss-project/green-recorder) [Green Recorder](https://github.com/foss-project/green-recorder) - A simple desktop recorder for Linux systems, supports recording audio and video on almost all Linux interfaces and Wayland display server on GNOME session.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/kazam) [Kazam](https://launchpad.net/kazam) - An easy to use and very intuitive screen recording program that will capture the content of your screen and record a video file that can be played by any video player that supports VP8/WebM video format.
- [![Open-Source Software][oss icon]](https://github.com/jp9000/OBS) [OBS Studio](https://obsproject.com/) - Free and open source software for video recording and live streaming. Download and start streaming quickly and easily on Windows, Mac or Linux. Share your gaming, art and entertainment with the world.
- [![Open-Source Software][oss icon]](https://github.com/phw/peek) [Peek](https://github.com/phw/peek) - Simple animated GIF screen recorder with an easy to use interface.
- [![Open-Source Software][oss icon]](https://github.com/colinkeenan/silentcast) [Silentcast](https://github.com/colinkeenan/silentcast) - Silentcast can create MKV screencasts and also output to an animated GIF.
- [![Open-Source Software][oss icon]](https://github.com/MaartenBaert/ssr) [SimpleScreenRecorder](http://www.maartenbaert.be/simplescreenrecorder/) - SimpleScreenRecorder is a feature-rich screen recorder that supports X11 and OpenGL. It has a Qt-based graphical user interface.
- [![Open-Source Software][oss icon]](https://github.com/vkohaupt/vokoscreenNG) [vokoscreenNG](https://linuxecke.volkoh.de/vokoscreen/vokoscreen.html) - A free, multilingual and easy to use screencast recorder with audio for Linux. It has many features.

#### Screenshot

- [![Open-Source Software][oss icon]](https://github.com/lupoDharkael/flameshot) [Flameshot](https://github.com/lupoDharkael/flameshot) - Powerful yet simple to use screenshot software.
- [![Open-Source Software][oss icon]](https://github.com/olav-st/screencloud) [Screencloud](http://screencloud.net/) - ScreenCloud is an easy to use screenshot sharing tool consisting of a cross-platform client and a sharing website: http://screencloud.net/.
- [![Open-Source Software][oss icon]](https://github.com/ShareX/ShareX) [ShareX](https://getsharex.com) - ShareX is a free and open source program that lets you capture or record any area of your screen and share it with a single press of a key. It also allows uploading images, text or other types of files to over 80 supported destinations you can choose from.
- [![Open-Source Software][oss icon]](https://launchpad.net/shutter/) [Shutter](http://shutter-project.org/) - Shutter is a feature-rich screenshot program for Linux based operating systems such as Ubuntu.

#### Streaming

- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/minidlna) [ReadyMedia](http://minidlna.sourceforge.net/) - Formerly known as **MiniDLNA**, ReadyMedia is a is a simple, lightweight media server software, with the aim of being fully compliant with DLNA/UPnP-AV clients. The MiniDNLA daemon serves media files (music, pictures, and video) to clients on a network such as smartphones, portable media players, televisions, other computers and some gaming systems.

#### Video editor

- [![Open-Source Software][oss icon]](https://github.com/cinelerra-cv-team/cinelerra-cv) [Cinelerra-cv](http://cinelerra.org/) - Professional video editing and compositing environment.
- [![Open-Source Software][oss icon]](https://github.com/jliljebl/flowblade) [Flowblade](https://github.com/jliljebl/flowblade/releases/tag/1.12.2) - A multitrack non-linear video editor for Linux.
- [![Open-Source Software][oss icon]](https://github.com/KDE/kdenlive) [Kdenlive](https://kdenlive.org/) - Kdenlive is a Non-Linear Video Editor, which is much more powerful than beginners’ (linear) editors.
- ![Nonfree][money icon] [Lightworks](https://www.lwks.com/) - Professional non-linear video editing program with a free version available.
- [![Open-Source Software][oss icon]](https://github.com/OpenShot/openshot-qt) [OpenShot](http://www.openshot.org/) - OpenShot is a free, simple-to-use, feature-rich video editor for Linux.
- [![Open-Source Software][oss icon]](https://github.com/mltframework/shotcut) [Shotcut](https://www.shotcut.org/) - Shotcut is a free, open source, cross-platform video editor with support for hundreds of audio and video formats and codecs and a sleek, intuitive interface.
- [![Open-Source Software][oss icon]](https://gitlab.gnome.org/GNOME/pitivi) [Pitivi](http://www.pitivi.org/) - A free video editor with a beautiful and intuitive user interface, a clean codebase and a fantastic community.
- [![Open-Source Software][oss icon]](https://github.com/ozmartian/vidcutter) [Vidcutter](http://vidcutter.ozmartians.com/) - Cross-platform Qt5 based app for quick and easy video trimming/splitting and merging/joining for simple quick edits.

### Internet

#### Browser

- [![Open-Source Software][oss icon]](https://github.com/brave/browser-laptop) [Brave](https://brave.com/) - Brave is a fast, good desktop browser for macOS, Windows, and Linux.
- [Chrome](https://www.google.com/chrome/browser/desktop/index.html) - A popular Web Browser with a lot of plugins/apps.
- [![Open-Source Software][oss icon]](https://www.chromium.org/) [Chromium](http://askubuntu.com/questions/250773/how-do-i-install-chromium-from-the-command-line) - Chromium is an open-source browser project that aims to build a safer, faster, and more stable way for all users to experience the web.
- [![Open-Source Software][oss icon]](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide) [Firefox](https://www.mozilla.org/en-US/firefox/new/) - A popular Web Browser with a lot of plugins/apps.
- [![Open-Source Software][oss icon]](https://git.savannah.gnu.org/cgit/gnuzilla.git) [IceCat](https://www.gnu.org/software/gnuzilla/) - GNU version of Firefox built for privacy, using only free software and free of trademarks.
- [![Open-Source Software][oss icon]](https://launchpad.net/~midori/+archive/ubuntu/ppa). [Midori](https://astian.org/midori-browser/download/) - A lightweight free browser that runs well on low spec systems.
- [![Open-Source Software][oss icon]](https://github.com/minbrowser/min) [Min](https://minbrowser.github.io/min) - A smarter, faster web browser.
- [Opera](http://www.opera.com/) - Opera browser is everything you need to do more on the web.
- [![Open-Source Software][oss icon]](https://github.com/qutebrowser/qutebrowser) [QuteBrowser](https://www.qutebrowser.org/) - A keyboard-driven, vim-like browser based on PyQt5.
- [Vivaldi](https://vivaldi.com/?lang=en) - A new and rising browser with a lot of customizations.
- [Yandex](https://browser.yandex.com/desktop/main/) - Fast and convenient browser.

#### Supportive Tool

- [Clipgrab](https://clipgrab.org/) - A friendly downloader for YouTube and other sites.
- [![Open-Source Software][oss icon]](https://gitweb.torproject.org/tor.git) [Tor](https://www.torproject.org/) - Tor is free software and an open network that helps you defend against traffic analysis, a form of network surveillance that threatens personal freedom and privacy.
- [![Open-Source Software][oss icon]](https://github.com/rg3/youtube-dl) [youtube-dl](https://github.com/rg3/youtube-dl) - Command line video downloader from youtube.com and about other thousand video platforms. It's really awesome, at least for me.
- [![Open-Source Software][oss icon]](https://github.com/MrS0m30n3/youtube-dl-gui) [youtube-dlg](https://mrs0m30n3.github.io/youtube-dl-gui/#downloads) - Youtube-dlg is a GUI for youtube-dl and allows for simple copy and paste from all youtube-dl compatible websites. It can auto-update youtube-dl as well as process a list of URL's in parallel.
- [![Open-Source Software][oss icon]](https://github.com/zerotier/ZeroTierOne) [Zerotier](https://my.zerotier.com) - Zerotier is a program that creates a Virtual Network for only your devices with end to end encyrption over the internet. By default Zerotier will manage your virtual network but you can switch to a self-managed network if you prefer.

#### Web Service Client

- [![Open-Source Software][oss icon]](https://cgit.kde.org/akregator.git/) [Akregator](https://userbase.kde.org/Akregator) - A KDE Feed Reader.
- [![Open-Source Software][oss icon]](http://choqok.gnufolks.org/) [Choqok](http://choqok.gnufolks.org/) - Choqok is a Qt5 client for Twitter, GNU Social, Friendica and Pump.IO.
- [![Open-Source Software][oss icon]](https://github.com/baedert/corebird) [Corebird](http://corebird.baedert.org/) - Corebird is native gtk+ twitter desktop client.
- [![Open-Source Software][oss icon]](https://github.com/jangernert/FeedReader) [FeedReader](https://github.com/jangernert/FeedReader) - A modern desktop application designed to complement existing web-based RSS accounts, combines all the advantages of web based services and modern desktop application.
- [![Open-Source Software][oss icon]](https://github.com/jeena/FeedTheMonkey) [FeedTheMonkey](https://github.com/jeena/FeedTheMonkey/releases) - FeedTheMonkey is a desktop client for TinyTinyRSS.
- [![Open-Source Software][oss icon]](https://github.com/vinszent/gnome-twitch) [GnomeTwitch](http://gnome-twitch.vinszent.com/) - Enjoy Twitch on your GNU/Linux desktop with this Twitch non-Adobe-flash client.
- [![Open-Source Software][oss icon]](https://github.com/EragonJ/Kaku) [Kaku](https://github.com/EragonJ/Kaku/releases) - An opensource youtube music player for Ubuntu.
- [![Open-Source Software][oss icon]](https://github.com/popcorn-official/) [Popcorntime](https://popcorntime.sh/) - Watch torrent movies instantly.

### Office

#### Accounting

- [![Open-Source Software][oss icon]](https://github.com/Gnucash/) [GnuCash](https://www.gnucash.org/) - GnuCash is a free software accounting program that implements a double-entry bookkeeping system. It was initially aimed at developing capabilities similar to Intuit, Inc.'s Quicken application, but also has features for small business accounting.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/homebank) [HomeBank](http://homebank.free.fr/en/index.php) - HomeBank is a free software that will assist you to manage your personal accounting.
- [![Open-Source Software][oss icon]](https://github.com/KDE/kmymoney) [KMyMoney](https://kmymoney.org/) - KMyMoney is the personal finance manager by KDE. Its operation is similar to Microsoft Money and Quicken.
- [![Open-Source Software][oss icon]](https://cgit.kde.org/skrooge.git) [Skrooge](https://skrooge.org/) - A personal finances manager, powered by KDE.

#### Office Suites

- [![Open-Source Software][oss icon]](https://cgit.kde.org/calligra.git/) [Caligra Office](https://www.calligra.org/) - offers a comprehensive set of 8 applications which satisfies the office, graphics and management needs.
- [![Open-Source Software][oss icon]](https://www.libreoffice.org/about-us/source-code/) [LibreOffice](https://www.libreoffice.org/) - Arguably the most popular office suite for Linux, it is very heavily developed and widely known.
- [![Open-Source Software][oss icon]](https://github.com/ONLYOFFICE) [OnlyOffice](https://www.onlyoffice.com/) - An office suite that charges for a cloud version of itself, but is free for other uses.
- [WPS office](http://wps-community.org/) - A popular office suite in China, but is fully translated and functions well in English.

#### LaTeX

- [![Open-Source Software][oss icon]](https://github.com/alexandervdm/gummi) [Gummi](https://gummi.app/) - Simple latex editor with templates, spell check, and wizards.
- [![Open-Source Software][oss icon]](https://git.gnome.org/browse/latexila) [LaTeXila](https://wiki.gnome.org/Apps/LaTeXila) - LaTeXila is a LaTeX editor for the GNOME desktop.
- [![Open-Source Software][oss icon]](https://github.com/yihui/lyx) [LyX](http://www.lyx.org/) - Mature document editor that renders into LaTeX.
- [![Open-Source Software][oss icon]](https://www.tug.org/texlive/build.html) [TexLive](https://www.tug.org/texlive/) - TeX Live is an easy way to get up and running with the TeX document production system.
- [![Open-Source Software][oss icon]](https://savannah.gnu.org/projects/texmacs) [TeXmacs](http://www.texmacs.org/) - Free scientific text editor, inspired by TeX and GNU Emacs. WYSIWYG editor and CAS-interface.
- [![Open-Source Software][oss icon]](http://www.xm1math.net/texmaker/download.html) [Texmaker](http://www.xm1math.net/texmaker/) - Free cross-platform LaTeX editor.
- [![Open-Source Software][oss icon]](https://github.com/TeXworks/texworks) [TeXworks](https://www.tug.org/texworks/) - TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents, with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean, simple interface accessible to casual and non-technical users.

#### Markdown

- [![Open-Source Software][oss icon]](http://github.com/wereturtle/ghostwriter) [Ghost Writer](https://ghostwriter.kde.org/) - A distraction-free Markdown editor for Windows and Linux.
- [![Open-Source Software][oss icon]](https://github.com/jamiemcg/remarkable) [Remarkable](https://remarkableapp.github.io/) - A capable markdown editor that uses a variant of GitHub Flavored Markdown (GFM)
- [Typora](https://typora.io/) - A Minimal markdown editor.

#### Novel Writing

- [![Open-Source Software][oss icon]](https://github.com/andreafeccomandi/bibisco) [Bibisco](http://www.bibisco.com/) - A novel writing software with focus on ideas and characters.
- [![Open-Source Software][oss icon]](https://github.com/olivierkes/manuskript) [Manuskript](http://www.theologeek.ch/manuskript/) - Manuskript is a perfect tool for those writer who like to organize and plan everything before writing.
- [![Open-Source Software][oss icon]](https://github.com/jacquetc/skribisto) [Skribisto](www.skribisto.eu) - Software for writers
- [![Open-Source Software][oss icon]](https://github.com/scribusproject/scribus) [Scribus](https://www.scribus.net/downloads/) - Scribus is a desktop publishing application designed for layout, typesetting, and preparation of files for professional-quality image-setting equipment. It can also create animated and interactive PDF presentations and forms.
- [![Open-Source Software][oss icon]](https://github.com/trelby/trelby) [Trelby](http://www.trelby.org/) - Trelby is simple, fast and elegantly laid out to make screenwriting simple.

### Productivity

#### Automation

- [![Open-Source Software][oss icon]](https://github.com/Jmgr/actiona) [Actionaz](http://actionaz.org/) - An utility for task automation Ubuntu/Linux.
- [![Open-Source Software][oss icon]](https://github.com/autokey/autokey) [Autokey](https://github.com/autokey/autokey) - A desktop automation utility for Linux allows you to manage collection of scripts and phrases, and assign abbreviations and hotkeys to these.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/caffeine) [Caffeine](https://launchpad.net/caffeine) - Prevents Ubuntu from automatically going to sleep.

#### Dock

- [![Open-Source Software][oss icon]](https://github.com/Cairo-Dock) [Cairo-Dock](http://glx-dock.org/) - Cairo-Dock is a desktop interface that takes the shape of docks, desklets, panel, etc.
- [![Open-Source Software][oss icon]](https://launchpad.net/docky/+download) [Docky](http://wiki.go-docky.com/index.php?title=Welcome_to_the_Docky_wiki) - Docky is a full fledged dock application that makes opening common applications and managing windows easier and quicker.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/plank) [Plank](https://launchpad.net/plank) - Plank is meant to be the simplest dock of apps on the planet.

#### Local Search

- [![Open-Source Software][oss icon]](https://github.com/albertlauncher/albert) [Albert](https://github.com/albertlauncher/albert) - An awesome application launcher for the Linux desktop
- [![Open-Source Software][oss icon]](https://github.com/DoTheEvo/ANGRYsearch) [AngrySearch](https://github.com/DoTheEvo/ANGRYsearch) - Linux file search, instant results as you type.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/catfish-search) [Catfish](https://launchpad.net/catfish-search) - Catfish is a versatile file searching tool.
- [![Open-Source Software][oss icon]](https://github.com/KELiON/cerebro) [Cerebro](https://cerebroapp.com/) - Open-source productivity booster with a brain / MacOS-Spotlight alternative.
- [![Open-Source Software][oss icon]](https://github.com/cboxdoerfer/fsearch) [fsearch](https://github.com/cboxdoerfer/fsearch) - A fast file search utility for Unix-like systems based on GTK+3. Wildcard support,RegEx support,Filter support.
- [![Open-Source Software][oss icon]](https://github.com/p-e-w/plotinus) [Plotinus](https://github.com/p-e-w/plotinus) - A searchable command palette in every modern GTK+ application.

#### Miscellaneous

- [![Open-Source Software][oss icon]](https://code.launchpad.net/anoise) [Ambient Noise](http://anoise.tuxfamily.org/) - An ambient noise generator for Linux.
- [![Open-Source Software][oss icon]](https://github.com/jarun/bcal) [bcal](https://github.com/jarun/bcal) - Perform storage conversions and calculations.
- [![Open-Source Software][oss icon]](https://github.com/hluk/CopyQ) [CopyQ](http://hluk.github.io/CopyQ/) -CopyQ is advanced clipboard manager with editing and scripting features.
- [f.lux](https://justgetflux.com/linux.html) - A program that reddens your display to help you sleep better.
- [![Open-Source Software][oss icon]](https://github.com/thezbyg/gpick) [Gpick](http://www.gpick.org/) - Gpick allows you to sample any color from anywhere on your desktop, and it also provides some other advanced features!
- [![Open-Source Software][oss icon]](https://github.com/jarun/pdd) [pdd](https://github.com/jarun/pdd) - Tiny date, time diff calculator.
- [![Open-Source Software][oss icon]](https://github.com/jonls/redshift) [Redshift](http://jonls.dk/redshift/) - Redshift adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less if you are working in front of the screen at night.
- [![Open-Source Software][oss icon]](http://www.speedcrunch.org/) [SpeedCrunch](http://www.speedcrunch.org/) - A nice, open source, high-precision scientific calculator.
- [![Open-Source Software][oss icon]](https://github.com/jml/undistract-me) [Undistract me](https://github.com/jml/undistract-me) - Notifies you when long-running terminal commands complete.
- [Xmind](http://www.xmind.net/) - A mind mapping tool.

#### Note Taking

- [![Open-Source Software][oss icon]](https://github.com/KDE/basket) [Basket Note Pads](https://apps.kde.org/basket/) - This multi-purpose note-taking application helps you to easily take all sort of notes.
- [![Open-Source Software][oss icon]](https://github.com/BoostIO/BoostNote-App) [Boostnote](https://boostnote.io/) - Boostnote is an open source note-taking app made for programmers just like you.
- ![Nonfree][money icon] [Inkdrop](https://www.inkdrop.info/) - The Note-Taking App for Markdown Lovers with simple interface, seemless security and powerful APIs.
- [![Open-Source Software][oss icon]](https://github.com/laurent22/joplin) [Joplin](http://joplin.cozic.net) - a note taking and to-do application with synchronization capabilities for Windows, macOS, Linux, Android and iOS.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/nevernote/code/ci/master/tree/) [NixNote](https://sourceforge.net/projects/nevernote/) - An open source client for Evernote.
- [![Open-Source Software][oss icon]](https://github.com/notepadqq/notepadqq) [Notepadqq](https://notepadqq.com/s/) - Notepadqq is a Notepad++-like editor for the Linux desktop.
- [![Open-Source Software][oss icon]](https://github.com/nuttyartist/notes) [Notes](http://www.get-notes.com/) - A clean simple note taking app for Linux.
- [![Open-Source Software][oss icon]](https://github.com/patrikx3/onenote) [OneNote](https://www.corifeus.com/onenote) - Linux Electron OneNote.
- [![Open-Source Software][oss icon]](https://git.savannah.gnu.org/cgit/emacs/org-mode.git/) [Org mode](http://orgmode.org/) - Org mode is for keeping notes, maintaining TODO lists, planning projects, and authoring documents with a fast and effective plain-text system.
- [![Open-Source Software][oss icon]](https://github.com/Aseman-Land/Papyrus) [Papyrus](http://aseman.co/en/products/papyrus/) - Papyrus is a different note manager which is focusing on Security, Better user interface. Papyrus are trying to provide an easy to use and smart user interface for users.
- [![Open-Source Software][oss icon]](https://github.com/pbek/QOwnNotes) [QOwnNotes](https://github.com/pbek/QOwnNotes) - QOwnNotes is a plain-text file notepad and todo-list manager with markdown support and ownCloud / Nextcloud integration.
- [Simplenote](https://simplenote.com/) - A Cross platform notetaking app and Evernote competitor.
- [![Open-Source Software][oss icon]](https://github.com/spsdco/notes) [Springseed](https://github.com/spsdco/notes) - Simple and beautiful note taking app for daily user.
- [Stickynote](https://itsfoss.com/indicator-stickynotes-windows-like-sticky-note-app-for-ubuntu/) - Sticky notes on your Linux desktop.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Tomboy) [Tomboy](https://wiki.gnome.org/Apps/Tomboy) - Tomboy is a desktop note-taking application which is simple and easy to use.
- [![Open-Source Software][oss icon]](https://github.com/CellarD0-0r/whatever) [Whatever](https://github.com/CellarD0-0r/whatever) - An unofficial Evernote desktop client for Linux.
- [![Open-Source Software][oss icon]](https://github.com/wizteam/wizqtclient) [WizNote](https://github.com/wizteam/wizqtclient) - A cross-platform cloud based note-taking client.

#### Time and Task

- [![Open-Source Software][oss icon]](http://bazaar.launchpad.net/~joh/alarm-clock/trunk/files) [Alarm Clock](https://alarm-clock.pseudoberries.com/) - Alarm Clock is a fully-featured alarm clock for your GNOME panel or equivalent.
- [![Open-Source Software][oss icon]](https://git.calcurse.org/calcurse.git/) [calcurse](http://calcurse.org/) - A calendar and scheduling application for the command line.
- [California](https://wiki.gnome.org/Apps/California) - Complete Calendar app replacement which uses natural language for creating events.
- ![Nonfree][money icon] [Everdo](https://everdo.net/linux) - TODO list and Getting Things Done® app for all platforms. Beautiful, powerful, not SaaS, free version available.
- [![Open-Source Software][oss icon]](https://github.com/codito/gnome-pomodoro) [Gnome Pomodoro](https://gnomepomodoro.org/#download) - A full-featured pomodoro timer for GNOME.
- [![Open-Source Software][oss icon]](https://github.com/mank319/Go-For-It) [Go For It](http://manuel-kehl.de/projects/go-for-it/) - Go For It! is a simple and stylish productivity app, featuring a to-do list, merged with a timer that keeps your focus on the current task.
- [![Open-Source Software][oss icon]](https://github.com/mohamed-aziz/mytodo) [My Todo](https://github.com/mohamed-aziz/mytodo) - Mytodo is an open source to-do list program that puts you, the user, in command of everything.
- ![Nonfree][money icon] [Pomodone App](http://pomodoneapp.com/) - PomoDoneApp is the easiest way to track your workflow using Pomodoro technique®, on top of your current task management service.
- [![Open-Source Software][oss icon]](https://userbase.kde.org/RSIBreak) [RSIBreak](https://userbase.kde.org/RSIBreak) - RSIBreak takes care of your health and regularly breaks your work to avoid repetitive strain injury.
- [![Open-Source Software][oss icon]](https://git.tasktools.org/projects) [TaskWarrior](https://taskwarrior.org/) - Taskwarrior is Free and Open Source Software that manages your TODO list from the command line.
- [![Open-Source Software][oss icon]](https://github.com/todotxt/todo.txt-android) [Todo.txt](http://todotxt.com/) - todo.txt is a set of focused editors which help you manage your tasks with as few keystrokes and taps possible.
- [![Open-Source Software][oss icon]](https://github.com/kamhix/todoist-linux) [Todoist](https://github.com/kamhix/todoist-linux) - Unofficial client of Todoist, the cross-platform to-do manager with mobile apps, great UI and has some optional premium features.

#### Widget and Indicator

- [![Open-Source Software][oss icon]](https://launchpad.net/indicator-brightness) [Brightness](https://launchpad.net/indicator-brightness) - Brightness indicator for Ubuntu.
- [![Open-Source Software][oss icon]](https://launchpad.net/my-weather-indicator) [My Weather Indicator](http://ubuntuhandbook.org/index.php/2016/04/weather-indicator-desktop-widget-ubuntu-16-04/) - Weather indicator and widget for ubuntu.
- [![Open-Source Software][oss icon]](https://launchpad.net/recent-notifications) [Recent Noti](https://itsfoss.com/7-best-indicator-applets-for-ubuntu-13-10/) - An indicator for recent notification.

### Proxy

- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/ijbswa/) [Privoxy](https://www.privoxy.org/) - Privoxy is a non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk.
- [![Open-Source Software][oss icon]](https://github.com/haad/proxychains) [ProxyChains](https://github.com/haad/proxychains) - A tool that forces any TCP connection made by any given application to follow through proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy.
- [![Open-Source Software][oss icon]](https://github.com/shadowsocks/shadowsocks-qt5/releases) [Shadowsocks](https://shadowsocks.org/) - A secure socks5 proxy, designed to protect your Internet traffic.

### Security

- [![Open-Source Software][oss icon]](https://github.com/vrtadmin/clamav-devel/pulls) [ClamAV](https://www.clamav.net/) - ClamAV is an open source antivirus engine for detecting trojans, viruses, malware & other malicious threats.
- [![Open-Source Software][oss icon]](https://github.com/fail2ban/fail2ban) [Fail2ban](http://www.fail2ban.org/wiki/index.php/Main_Page) - Fail2ban scans log files (e.g. /var/log/apache/error_log) and bans IPs that show the malicious signs -- too many password failures, seeking for exploits, etc.
- [![Open-Source Software][oss icon]](https://github.com/firehol/firehol) [FireHOL](https://firehol.org) - Linux firewall (`iptables`) manager for humans.
- [![Open-Source Software][oss icon]](https://github.com/netblue30/firejail) [Firejail](https://firejail.wordpress.com/) - Firejail is a SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using [Linux namespaces](https://lwn.net/Articles/531114/) and [seccomp-bpf](https://l3net.wordpress.com/2015/04/13/firejail-seccomp-guide/).
- [![Open-Source Software][oss icon]](https://firehol.org/tutorial/fireqos-new-user/) [FireQoS](https://github.com/firehol/netdata/wiki/You-should-install-QoS-on-all-your-servers) - Linux QoS (`tc`) manager for humans.
- [![Open-Source Software][oss icon]](https://github.com/firewalld/firewalld) [Firewalld](https://github.com/firewalld/firewalld) - Firewalld provides a dynamically managed firewall with support for network or
  firewall zones to define the trust level of network connections or interfaces. [![Open-Source Software][oss icon]](https://github.com/firewalld/firewalld)
- [![Open-Source Software][oss icon]](https://git.gnupg.org/) [GnuPG](https://www.gnupg.org/) - GnuPG allows to encrypt and sign your data and communication, features a versatile key management system as well as access modules for all kinds of public key directories.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/gui-ufw) [GuFW](http://gufw.org/) - One of the easiest firewalls in the world of Linux.
- [![Open-Source Software][oss icon]](https://github.com/firehol/iprange) [IPrange](https://github.com/firehol/iprange) - A very fast command line utility for processing IP lists (merge, compare, exclude, etc).
- [![Open-Source Software][oss icon]](https://github.com/jarun/spy) [spy](https://github.com/jarun/spy) - Linux kernel mode debugfs keylogger.
- [![Open-Source Software][oss icon]](https://github.com/CISOfy/lynis) [Lynis](https://cisofy.com/lynis/) - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation optional.
- [![Open-Source Software][oss icon]](https://www.openbsd.org/anoncvs.html) [OpenSSH](http://www.openssh.com/) - OpenSSH Secure Shell Server and Client
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/passwordsafe/) [Password Safe](https://pwsafe.org/) - Password Safe allows you to safely and easily create a secured and encrypted user name/password list.
- [![Open-Source Software][oss icon]](https://git.zx2c4.com/password-store/) [Pass](https://www.passwordstore.org/) - The standard Unix password manager.
- [![Open-Source Software][oss icon]](https://wiki.gnome.org/Apps/Seahorse) [Seahorse](https://wiki.gnome.org/Apps/Seahorse) - A Gnome frontend for GnuPG.
- [![Open-Source Software][oss icon]](http://www.tcpdump.org/#source) [Tcpdump](http://www.tcpdump.org/) - TCP Debugging/Capture Tool.
- [![Open-Source Software][oss icon]](https://github.com/firehol/blocklist-ipsets) [Update-IPsets](https://iplists.firehol.org) - A manager for all cybercrime IP feeds that can download, convert and install netfilter `ipsets`.
- [![Open-Source Software][oss icon]](https://github.com/usbkey9/uktools) [Uktools](https://github.com/usbkey9/uktools) - Keep your system up-to-date with last kernel available. Possibility to clean old kernel too.

### Sharing Files

- [![Open-Source Software][oss icon]](https://github.com/aria2/aria2) [aria2](https://aria2.github.io/) - aria2 is a lightweight multi-protocol & multi-source command-line download utility.
- [CrossFTP](http://www.crossftp.com/ftp-client.htm) - CrossFTP makes it extremely simple to manage the FTP related tasks.
- [D-lan](https://www.d-lan.net/) - A free LAN file sharing software.
- [![Open-Source Software][oss icon]](http://dev.deluge-torrent.org/wiki/Development#SourceCode) [Deluge](http://deluge-torrent.org/) - Deluge is a lightweight, Free Software, cross-platform BitTorrent client.
- [Dropbox](https://www.dropbox.com/install?os=lnx) - Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily.
- [![Open-Source Software][oss icon]](https://filezilla-project.org/sourcecode.php) [Filezilla](https://filezilla-project.org/) - The free FTP solution.
- [Flareget](https://flareget.com/) - Full featured, multi-threaded download manager and accelerator.
- [![Open-Source Software][oss icon]](https://invent.kde.org/network/ktorrent) [KTorrent](https://www.kde.org/applications/internet/ktorrent/) - KTorrent is a BitTorrent application by KDE which allows you to download files using the BitTorrent protocol.
- [![Open-Source Software][oss icon]](https://github.com/meganz/MEGAsync) [Mega](https://mega.nz/#sync) - Easy automated syncing between your computers and your MEGA cloud drive.
- [![Open-Source Software][oss icon]](https://github.com/nitroshare/nitroshare-desktop) [NitroShare](https://nitroshare.net/) - Cross-Platform network file transfer application.
- [![Open-Source Software][oss icon]](https://github.com/owncloud) [ownCloud](https://owncloud.com/products/desktop-clients/) - The goal of ownCloud is to give you access to your files wherever you are.
- [![Open-Source Software][oss icon]](https://github.com/nextcloud) [nextCloud](https://nextcloud.com/) - an actively maintained fork of ownCloud, a suite of client-server software for creating and using file hosting services
- [![Open-Source Software][oss icon]](https://github.com/sidneys/pb-for-desktop) [PushBullet for desktop](https://sidneys.github.io/pb-for-desktop/) - The missing Desktop application for Pushbullet.
- [PushBullet](https://www.pushbullet.com/) - Pushbullet connects your devices, making them feel like one.
- [![Open-Source Software][oss icon]](https://github.com/qbittorrent/qBittorrent) [qBittorent](http://www.qbittorrent.org/) - The qBittorrent project aims to provide a Free Software alternative to µTorrent.
- [Quazaa](https://sourceforge.net/projects/quazaa/) - A cross platform multi-network peer-to-peer (P2P) file-sharing client.
- [![Open-Source Software][oss icon]](https://github.com/haiwen/seafile) [Seafile](https://www.seafile.com/en/home/) - Seafile is an enterprise file hosting platform with high reliability and performance. Put files on your own server. Sync and share files across different devices, or access all the files as a virtual disk.
- [SpiderOak](https://spideroak.com/) - Real-time collaboration for teams and businesses that care about privacy
- [![Open-Source Software][oss icon]](https://github.com/syncthing/syncthing) [Syncthing](https://syncthing.net/) - Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized.
- [Teamviewer](https://www.teamviewer.com/) - PC remote control/remote access software, free for personal use.
- [Tixati](https://www.tixati.com/) - Freeware, advanced featured torrent client, a web user interface is included.
- [![Open-Source Software][oss icon]](https://trac.transmissionbt.com/browser/trunk) [Transmission](https://www.transmissionbt.com/download/) - Simple, lightweight, multi-platform torrent client.
- [![Open-Source Software][oss icon]](https://github.com/leonsoft-kras/transmisson-remote-gui) [Transmission Remote GUI](https://sourceforge.net/projects/transgui/) - Transmission Remote GUI is a feature rich cross platform front-end to remotely control a Transmission Bit-Torrent client daemon via its RPC protocol.
- [![Open-Source Software][oss icon]](https://ugetdm.com/downloads/source-code/) [uGet](http://ugetdm.com/) - A download manager that can monitor the clipboard for downloadable links, and can create a list of downloads, and run them in parallel.
- [![Open-Source Software][oss icon]](http://dev.vuze.com/) [Vuze](http://www.vuze.com) - Bittorrent Client is an end-to-end software application for all your torrent needs.
- [![Open-Source Software][oss icon]](https://github.com/webtorrent/webtorrent-desktop) [Web Torrent Desktop](https://webtorrent.io/desktop/) - Web Torrent Desktop is for streaming torrents which connects to both BitTorrent and WebTorrent peers.
- [![Open-Source Software][oss icon]](https://github.com/warner/magic-wormhole) [Wormhole](https://github.com/warner/magic-wormhole) - get arbitrary-sized files and directories (or short pieces of text) from one computer to another safely.

### Terminal

- [![Open-Source Software][oss icon]](https://github.com/jwilm/alacritty) [Alacritty](https://github.com/jwilm/alacritty) - A cross-platform, GPU-accelerated terminal emulator.
- [![Open-Source Software][oss icon]](https://github.com/Swordfish90/cool-retro-term) [Cool Retro Term](https://github.com/Swordfish90/cool-retro-term) - A good looking terminal that mimicks the old cathode display.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/dban/) [DBAN](https://dban.org/) - Delete information stored on hard disk drives (HDDs) in PC laptops, desktops or servers.
- [![Open-Source Software][oss icon]](https://github.com/GNOME) [GnomeTerminal](https://help.gnome.org/users/gnome-terminal/stable/) - A widely preinstalled terminal emulator in Linux world.
- [![Open-Source Software][oss icon]](https://github.com/Guake/guake) [Guake](http://guake.org/) - Guake is a top-down terminal for Gnome.
- [![Open-Source Software][oss icon]](https://github.com/zeit/hyper) [Hyper](https://hyper.is/) - A terminal built on web technologies.
- [![Open-Source Software][oss icon]](https://github.com/kovidgoyal/kitty) [Kitty](https://github.com/kovidgoyal/kitty) - Cross-platform, fast, feature full, OpenGL based terminal emulator.
- [![Open-Source Software][oss icon]](https://github.com/KDE/konsole) [Konsole](https://konsole.kde.org/) - An alternative terminal emulator for KDE desktop environment.
- [![Open-Source Software][oss icon]](rxvt.http://cvs.schmorp.de/rxvt-unicode/) [RXVT-Unicode](http://software.schmorp.de/pkg/rxvt-unicode.html) - rxvt-unicode is a fork of the well known terminal emulator.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/rxvt/) [RXVT](https://rxvt.sourceforge.net/) - A terminal emulator for X11, a popular replacement for the standard ‘xterm’.
- [![Open-Source Software][oss icon]](https://launchpad.net/sakura) [Sakura](https://launchpad.net/sakura) - Simple but powerful libvte based terminal emulator, supporting utf-8 and input methods as provided by gtk+ and pango libraries.
- [![Open-Source Software][oss icon]](https://launchpad.net/terminator) [Terminator](http://gnometerminator.blogspot.com/p/introduction.html) - It’s quite clear that the most powerful terminal emulator on Linux is the feature-filled Terminator.
- [![Open-Source Software][oss icon]](https://github.com/billiob/terminology) [Terminology](https://www.enlightenment.org/about-terminology) - The pretty and lightweight terminal from the Enlightenment Desktop, it's highly configurable, it works in X11, under a Wayland compositor and even directly in the framebuffer on Linux. Replace your boring text-mode VT with a graphical one that requires no display system.
- [![Open-Source Software][oss icon]](https://github.com/Eugeny/terminus) [Terminus](https://eugeny.github.io/terminus/) - modern, highly configurable terminal app based on web technologies.
- [![Open-Source Software][oss icon]](https://github.com/thestinger/termite) [Termite](https://github.com/thestinger/termite) - A keyboard-centric VTE-based terminal, aimed at use within a window manager with tiling and/or tabbing support.
- [![Open-Source Software][oss icon]](https://github.com/nonstop/termit/wiki) [Termit](https://github.com/nonstop/termit/wiki) - Simple terminal emulator based on vte library, extensible via Lua.
- [Termius](https://www.termius.com/) - cross-platform terminal with built-in SSH and Telnet.
- [![Open-Source Software][oss icon]](https://github.com/gnunn1/tilix) [Tilix](https://gnunn1.github.io/tilix-web/) - A tiling terminal emulator for Linux using GTK+ 3.
- [![Open-Source Software][oss icon]](https://github.com/tmux/tmux) [Tmux](https://tmux.github.io/) - It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. And do a lot more.
- [![Open-Source Software][oss icon]](https://github.com/cosmos72/twin) [Twin](https://github.com/cosmos72/twin/) - Fast, lightweight text-mode window environment with mouse support. Enables multiple terminals in a single Linux console, terminal or X11 window. It can be detached (keeps running in background) and reattached to a different console, terminal or X11 server. Works on Linux, Mac OS X and BSD
- [![Open-Source Software][oss icon]](https://github.com/railsware/upterm) [Upterm](https://github.com/railsware/upterm) - Upterm (formerly Black Screen) is an IDE in the world of terminals. Strictly speaking, it's both a terminal emulator and an interactive shell based on [Electron](https://electron.atom.io/).
- [![Open-Source Software][oss icon]](http://invisible-island.net/xterm/) [Xterm](http://invisible-island.net/xterm/) - The Xterm program is a terminal emulator for the X Window System. It provides DEC VT102 and Tektronix 4014 compatible terminals for programs that can't use the window system directly.
- [![Open-Source Software][oss icon]](https://invent.kde.org/utilities/yakuake) [Yakuake](https://apps.kde.org/yakuake/) - A Quake-style terminal emulator based on KDE Konsole technology.

### Utilities

- [![Open-Source Software][oss icon]](https://github.com/mildred/alien) [Alien Package Converter](https://sourceforge.net/projects/alien-pkg-convert/) - Package converter. Converts between RPM, DPKG, SLP, and TGZ package formats.
- [![Open-Source Software][oss icon]](https://github.com/angryip/ipscan) [Angry IP Scanner](http://angryip.org/) - Fast and friendly network scanner.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/~teejee2008/apt-toolkit/trunk) [Aptik](https://teejeetech.com/2019/07/14/aptik-v19-07/) - A tool for you to organize your Favorite PPAs and manage Packages Easily.
- [![Open-Source Software][oss icon]](https://github.com/bleachbit/bleachbit) [Bleach bit](https://www.bleachbit.org/) - BleachBit quickly frees disk space and tirelessly guards your privacy. Free cache, delete cookies, clear Internet history, shred temporary files, delete logs, and more.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/brasero) [Brasero](https://wiki.gnome.org/Apps/Brasero) - A capable CD/DVD burner.
- [![Open-Source Software][oss icon]](https://github.com/chrisallenlane/cheat) [Cheat](https://github.com/chrisallenlane/cheat) - Cheat allows you to create and view interactive cheatsheets on the command-line.
- [![Open-Source Software][oss icon]](https://clonezilla.org/related-links/) [Clonezilla](http://clonezilla.org/) - Clonezilla is a partition and disk imaging/cloning program similar to True Image® or Norton Ghost®.
- [![Open-Source Software][oss icon]](http://convertall.bellz.org/download.html) [Convertall](https://sourceforge.net/projects/convertall/) - A program that can convert many units of measurement to other units.
- [![Open-Source Software][oss icon]](https://launchpad.net/cpug) [CPU-G](http://www.omgubuntu.co.uk/2016/09/monitor-battery-life-ubuntu-cpu-g) - Easy monitoring the battery life of your Ubuntu laptop.
- [![Open-Source Software][oss icon]](https://github.com/chamfay/Curlew) [Curlew](https://github.com/chamfay/Curlew) - A GTK media converter for the GNOME desktop.
- [![Open-Source Software][oss icon]](https://github.com/thjaeger/easystroke) [EasyStroke](https://github.com/thjaeger/easystroke/wiki#download) - Easystroke is a gesture-recognition application for X11.
- [![Open-Source Software][oss icon]](https://github.com/OzymandiasTheGreat/emoji-keyboard) [Emoji Keyboard](https://github.com/OzymandiasTheGreat/emoji-keyboard) - Virtual keyboard-like emoji picker for Linux.
- [![Open-Source Software][oss icon]](https://github.com/SpiderOak/Encryptr) [Encryptr](https://spideroak.com/personal/encryptr) - Encryptr is a zero-knowledge, cloud-based e-wallet / password manager powered by Crypton.
- [Enpass](https://www.enpass.io/) - Enpass makes your life easy by securely managing your passwords and important information.
- [![Open-Source Software][oss icon]](https://github.com/resin-io/etcher) [Etcher](https://www.balena.io/etcher/) - Flash OS images to SD cards & USB drives, safely and easily.
- [![Open-Source Software][oss icon]](https://github.com/FreeRDP/FreeRDP) [FreeRDP](http://www.freerdp.com/) - FreeRDP is a free implementation of the Remote Desktop Protocol (RDP).
- [GD map](https://gdmap.sourceforge.net/) - A tool to visualize disk usage.
- [![Open-Source Software][oss icon]](https://github.com/antonio-malcolm/gloobus-preview) [Gloobus-Preview](https://github.com/antonio-malcolm/gloobus-preview) - It gives you a quick preview of your files. It's similar to [Sushi](https://github.com/GNOME/sushi)
- [![Open-Source Software][oss icon]](http://simmesimme.github.io/news/2016/08/24/gnome-pie-069) [GnomePie](http://simmesimme.github.io/news/2016/08/24/gnome-pie-069) - the circular app launcher for Linux desktops.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gparted) [GParted](http://gparted.org/) - Disk Partition utility for Linux.
- [![Open-Source Software][oss icon]](https://github.com/gramps-project/gramps) [Gramps](https://github.com/gramps-project/gramps) - Research, organize and share your family tree with Gramps.
- [![Open-Source Software][oss icon]](https://launchpad.net/indicator-cpufreq) [indicator-cpufreq](https://launchpad.net/indicator-cpufreq) - It provides the same functionality as the Gnome CPU frequency applet, but doesn't require Gnome panel and works under Unity.
- [![Open-Source Software][oss icon]](https://launchpad.net/ubuntu/+source/indicator-multiload) [indicator-multiload](https://launchpad.net/ubuntu/+source/indicator-multiload) - Graphical system load indicator for CPU, ram, etc.
- [![Open-Source Software][oss icon]](https://github.com/fossfreedom/indicator-sysmonitor) [Indicator-SysMonitor](https://github.com/fossfreedom/indicator-sysmonitor) - An Application Indicator showing cpu temperature, memory, network speed, cpu usage, public IP address and internet connection status.
- [![Open-Source Software][oss icon]](https://github.com/KDE/kdeconnect-kde) [KDE-Connect](https://community.kde.org/KDEConnect) - A tool, that allows one to integrate the Linux desktop with an Android smartphone and can be used to send files to and from the phone and the linux desktop, use the phone as a trackpad, control the desktop media player using the phone, and lots more.
- [![Open-Source Software][oss icon]](https://github.com/keepassxreboot/keepassxc) [KeePassXC](https://keepassxc.org/) - Cross platform password manager. A Community-maintained fork of KeePassX([dead](https://github.com/keepassx/keepassx/pull/204))
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/keepass/files/KeePass%202.x/) [KeePass](https://www.keepass.info/) - Windows focused password manager, with some cross platform support through Mono.
- [![Open-Source Software][oss icon]](https://github.com/keeweb/keeweb) [KeeWeb](https://github.com/keeweb/keeweb) - Free cross-platform password manager compatible with KeePass
- [![Open-Source Software][oss icon]](https://github.com/jordansissel/keynav) [Keynav](http://www.semicomplete.com/projects/keynav/) - Keynav is a piece of an on-going experiment to make pointer-driven interfaces easier and faster for users to operate. It lets you move the pointer quickly to most points on the screen with only a few key strokes.
- [![Open-Source Software][oss icon]](https://github.com/iabem97/komorebi) [Komorebi](https://github.com/iabem97/komorebi/releases) - Komorebi is a background manager for all Linux platforms, provides fully customizeable backgrounds that can be tweaked at any time.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/kvm/files/) [KVM](http://www.linux-kvm.org/page/Main_Page) - KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V).
- [LastPass](https://lastpass.com/misc_download2.php) - LastPass is a crossplatform freemium password management service that stores encrypted passwords in private accounts.
- [![Open-Source Software][oss icon]](https://github.com/mobile-shell/mosh) [Mosh](https://mosh.org/#getting) - Mosh is a Remote terminal application that allows roaming, supports intermittent connectivity, and provides intelligent local echo and line editing of user keystrokes.
- [![Open-Source Software][oss icon]](https://github.com/jiahaog/nativefier) [Nativefier](https://github.com/jiahaog/nativefier) - Make any web page a desktop application
- [![Open-Source Software][oss icon]](https://github.com/firehol/netdata) [NetData](https://my-netdata.io) - Next-gen web based real-time performance and health monitoring for physical and virtual servers, containers and IoT devices. It is also a distributed `statsd` server with automatic visualization for APM (applications performance monitoring).
- [![Open-Source Software][oss icon]](https://g.blicky.net/ncdu.git/) [Ncdu](https://dev.yorhel.nl/ncdu) - A disk usage analyzer with an ncurses interface.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/peaextractor/) [PeaExtractor](http://www.peazip.org/peaextractor-unace-unrar-unzip.html) A utility designed to unzip files and be as frictionless as possible, and easy to use as possible.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/peautils/) [PeaUtilities](http://www.peazip.org/peautils-hash-secure-delete.html) PeaUtils is a suite of file management utilities, including hash checksums, secure delete, and file comparisons.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/peazip/files/Resources/) [Peazip](http://www.peazip.org/) - A utility to unzip any of a huge variety of compression formats.
- [![Open-Source Software][oss icon]](https://github.com/pi-hole/pi-hole) [Pi-Hole](https://pi-hole.net) - Network-wide ad blocking via your own Linux hardware, using DNS filtering and re-direction Pi-Hole can block ads on a whole network, so Smartphones and Game Consoles can benefit from it in addition to computers.
- [PlexyDesk](https://www.omgubuntu.co.uk/2016/09/plexydesk-widgets-linux-desktop-ppa) - Plexydesk supports multiple widget workspaces/desktops on Linux.
- [![Open-Source Software][oss icon]](https://github.com/fenrus75/powertop) [Powertop](https://01.org/powertop/downloads) - A tool that can help diagnose issues with power consumption in Linux.
- [![Open-Source Software][oss icon]](http://git.wpitchoune.net/psensor.git/) [Psensor](http://wpitchoune.net/psensor/) - A graphical hardware temperature monitor for Linux.
- [![Open-Source Software][oss icon]](https://github.com/pulseaudio/pulseaudio) [Pulse Audio](https://wiki.ubuntu.com/PulseAudio) - Improve Linux Audio with customized Profiles.
- [![Open-Source Software][oss icon]](https://github.com/FreeRDP/Remmina) [Remmina](http://www.remmina.org/wp/) - A feature-rich remote desktop application for Linux and other UNIXes.
- [![Open-Source Software][oss icon]](https://github.com/sahib/rmlint) [rmlint](https://rmlint.readthedocs.io/en/latest/) - rmlint finds space waste and other broken things on your filesystem and offers to remove it.
- [![Open-Source Software][oss icon]](https://github.com/oguzhaninan/Stacer) [Stacer](https://github.com/oguzhaninan/Stacer) - The most well known Ubuntu System Optimizer.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/sushi) [Sushi](https://github.com/GNOME/sushi) - Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.
- [![Open-Source Software][oss icon]](http://download.savannah.nongnu.org/releases/synaptic/) [Synaptic](http://www.nongnu.org/synaptic/) - Synaptic is a graphical package management program for apt.
- [![Open-Source Software][oss icon]](https://launchpad.net/indicator-multiload) [Systemload](http://www.omgubuntu.co.uk/2014/06/system-monitor-indicator-ubuntu-ppa) - A program that shows current system load in a status bar.
- ![Open-Source Software][oss icon] [TightVNC](http://www.tightvnc.com/) - A Free, Lightweight, Fast and Reliable Remote Control / Remote Desktop Software.
- [TLP](http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) - An application that can help optimize battery life on Linux.
- [![Open-Source Software][oss icon]](https://github.com/Kilian/Trimage) [Trimage](https://trimage.org/) - A cross-platform tool for losslessly optimizing PNG and JPG files.
- [![Open-Source Software][oss icon]](https://github.com/gerardpuig/ubuntu-cleaner) [UbuntuCleaner](https://github.com/gerardpuig/ubuntu-cleaner) - Ubuntu Cleaner is a tool that makes it easy to clean your Ubuntu system.
- [![Open-Source Software][oss icon]](https://github.com/adgellida/ubunsys) [Ubunsys](https://github.com/adgellida/ubunsys) - An application designed to allow you to change in-depth system features without the command line.
- [![Open-Source Software][oss icon]](https://github.com/Ulauncher/Ulauncher/) [ULauncher](http://ulauncher.io/) - An application launcher for Linux.
- [![Open-Source Software][oss icon]](https://github.com/unetbootin/unetbootin) [Unetbootin](https://unetbootin.github.io) - UNetbootin allows you to create bootable Live USB drives for Ubuntu and other Linux distributions. You can either let UNetbootin download one of the many distributions supported out-of-the-box for you, or supply your own Linux .iso file.
- [USB network gate](https://www.eltima.com/products/usb-over-ip-linux/) - Allows you to share USB ports over a Network on Linux.
- [![Open-Source Software][oss icon]](https://github.com/peterlevi/variety-slideshow) [Variety](http://peterlevi.com/variety/) - Variety is an open-source wallpaper changer for Linux, packed with great features, yet slim and easy to use.
- [![Open-Source Software][oss icon]](https://www.virtualbox.org/wiki/Contributor_information) [Virtualbox](https://www.virtualbox.org/wiki/Downloads) - VirtualBox is a general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use.
- [![Open-Source Software][oss icon]](http://melloristudio.com/wallch/#code) [WallpaperChange](https://apps.ubuntu.com/cat/applications/raring/wallch/) - Automatically change your wallpaper.
- [![Open-Source Software][oss icon]](https://github.com/rcaelers/workrave) [Workrave](https://www.workrave.org/) - A program that assists in the recovery and prevention of Repetitive Strain Injury (RSI).
- [![Open-Source Software][oss icon]](https://github.com/KaOS-Community-Packages/xdm) [Xtreme Download Manager](http://xdman.sourceforge.net/) - A good download manager with fresh UI for Linux.

### Video

- [![Open-Source Software][oss icon]](https://github.com/xylosper/bomi) [Bomi Player](https://bomi-player.github.io/) - A powerful and easy-to-use multimedia player.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/cheese) [Cheese](https://wiki.gnome.org/Apps/Cheese) - Cheese uses your webcam to take photos and videos, applies fancy special effects and lets you share the fun with others.
- [![Open-Source Software][oss icon]](https://github.com/xbmc/xbmc) [Kodi](https://kodi.tv/about/) - An award-winning free and open source (GPL) software media center for playing videos, music, pictures, games, and more.
- [![Open-Source Software][oss icon]](https://github.com/pculture/miro) [Miro](http://www.getmiro.com/) - Free, and open video, music and internet TV application; it brings video channels from thousands of sources and has more free HD than any other platform.
- [![Open-Source Software][oss icon]](https://github.com/lettier/movie-monad) [Movie Monad](https://lettier.github.io/movie-monad) - A free and simple to use video player made with Haskell.
- [![Open-Source Software][oss icon]](http://www.mplayerhq.hu/design7/dload.html) [MPlayer](http://www.mplayerhq.hu/design7/news.html) - MPlayer is a movie player which runs on many systems, play any kind of videos.
- [![Open-Source Software][oss icon]](https://github.com/mpv-player/mpv) [MPV](https://www.mpv.io) - A free, open source, and cross-platform media player.
- [![Open-Source Software][oss icon]](https://sourceforge.net/p/smplayer/code/HEAD/tree/) [SMPlayer](http://smplayer.sourceforge.net/) - Free Media Player with built-in codecs. Play all audio and video formats.
- [![Open-Source Software][oss icon]](https://gitlab.com/jonata/subtitld) [Subtitld](https://subtitld.org/) - Subtitld เป็นซอฟต์แวร์โอเพ่นซอร์สสำหรับแก้ไข ถอดความ และสร้างคำบรรยาย
- [SVP](https://www.svp-team.com/w/index.php?title=Main_Page) - SVP allows you to watch any video on your desktop computer using frame interpolation as it is available on high-end TVs and projectors.
- [![Open-Source Software][oss icon]](https://www.videolan.org/vlc/download-sources.html) [VLC](http://www.videolan.org/vlc/index.html) - VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols.

### Wiki software

- [![Open-Source Software][oss icon]](https://git.joeyh.name/git/ikiwiki.git/) [ikiwiki](https://ikiwiki.info/) - ikiwiki is a wiki compiler. It converts wiki pages into HTML pages suitable for publishing on a website. Ikiwiki stores pages and history in a revision control system such as Subversion or Git.
- [![Open-Source Software][oss icon]](https://github.com/Jermolene/TiddlyDesktop) [TiddlyDesktop on GitHub](https://github.com/TiddlyDesktop) - [TiddlyDesktop on TiddlyWiki.com](https://github.com/TiddlyDesktop) - A desktop app for TiddlyWiki, an open-source personal wiki written in javascript, great if you're still searching for a good note-taking (and more) app.
- [![Open-Source Software][oss icon]](https://launchpad.net/zim) [Zim](https://zim-wiki.org/) - A graphical text editor used to maintain a collection of wiki pages, great for notes and documents. Stored in plain text files for easy version control.

### Others

- [![Open-Source Software][oss icon]](https://displaycal.net/#download) [DisplayCAL](https://displaycal.net/) - Open Source Display Calibration and Characterization powered by ArgyllCMS.
- [![Open-Source Software][oss icon]](https://github.com/fontforge/fontforge) [FontForge](https://fontforge.github.io) - Free (libre) font editor for Windows, Mac OS X and GNU+Linux.
- [![Open-Source Software][oss icon]](https://code.launchpad.net/grub-customizer) [GrubCustomizer](https://launchpad.net/grub-customizer) - Grub Customizer is a graphical interface to configure the GRUB2/BURG settings and menuentries.
- [![Open-Source Software][oss icon]](https://github.com/bohoomil/fontconfig-ultimate) [Infinality bundle & fonts](https://github.com/bohoomil/fontconfig-ultimate) - _Pre-note: Infinality is currently not maintained anymore by the creator, if on rolling release operating systems, expect breakage_. Infinality bundle & fonts is an Open Source project aimed at Linux administrators and individual users who are looking for a hassle-free way of improving the quality of font rendering.
- [![Open-Source Software][oss icon]](https://github.com/MycroftAI/mycroft-core) [Mycroft](https://github.com/MycroftAI/mycroft-core) - Mycroft is a hackable open source voice assistant.
- [![Open-Source Software][oss icon]](https://github.com/lah7/polychromatic) [Polychromatic](https://github.com/lah7/polychromatic) - Graphical front end and tray applet for configuring Razer peripherals on GNU/Linux.

## Command Line Utilities

- [![Open-Source Software][oss icon]](https://github.com/jarun/Buku) [Buku](https://github.com/jarun/Buku) - A Command line bookmark manager.
- [![Open-Source Software][oss icon]](https://github.com/AlDanial/cloc) [Cloc](https://github.com/AlDanial/cloc) - Count Lines of Code: cloc counts blank lines, comment lines, and physical lines of source code in many programming languages.
- [![Open-Source Software][oss icon]](https://github.com/athityakumar/colorls) [Color LS](http://www.omgubuntu.co.uk/2017/07/add-bling-ls-bash-command-colorls) - Color Ls is a Ruby Gem that spices up the ls command and shows more visually than ls does without additional commands.
- [![Open-Source Software][oss icon]](https://github.com/chronitis/curseradio) [curseradio](https://github.com/chronitis/curseradio) - Command line radio player.
- [![Open-Source Software][oss icon]](https://github.com/ssimunic/Daily-Reddit-Wallpaper) [Daily Reddit Wallpaper](https://github.com/ssimunic/Daily-Reddit-Wallpaper) - Change your wallpaper to the most upvoted image of the day from /r/wallpapers or any other subreddit on system startup.
- [![Open-Source Software][oss icon]](https://github.com/jarun/ddgr) [ddgr](https://github.com/jarun/ddgr) - DuckDuckGo from the command line.
- [![Open-Source Software][oss icon]](https://github.com/balena-io/balena-cli) [Balena CLI](https://www.balena.io/docs/reference/balena-cli/) - The Balena CLI is a command-line tool that aims to provide all the benefits of the Balena desktop application in a way that can be run from a terminal, or even used from a script.
- [![Open-Source Software][oss icon]](https://github.com/ogham/exa) [exa](https://the.exa.website/) - exa is a modern replacement for ls.
- [![Open-Source Software][oss icon]](https://github.com/LubuntuFu/fishfry) [Fishfry](https://github.com/LubuntuFu/fishfry) - replaces fish history with a history tailored to pentesters for efficiency and newbie pentesters for learning.
- [![Open-Source Software][oss icon]](https://github.com/junegunn/fzf) [fzf](https://github.com/junegunn/fzf) - A general-purpose command-line fuzzy finder with interactive filter and preview feature for things like files, command history, git commits, hostnames, etc.
- [![Open-Source Software][oss icon]](https://github.com/heppu/gkill) [Gkill](https://github.com/heppu/gkill) - An interactive process killer for Linux.
- [![Open-Source Software][oss icon]](https://github.com/jarun/googler) [Googler](https://itsfoss.com/review-googler-linux/) - A program that can Google anything right in the command line.
- [![Open-Source Software][oss icon]](https://github.com/nicolargo/glances) [Glances](https://nicolargo.github.io/glances/) - Glances is a system monitoring terminal application that shows you your disk usage, ram usage, and cpu usage in a very friendly way using the Ncurses programming library. It is tolerant to windows resizing, and very low on system ram useage.
- [![Open-Source Software][oss icon]](https://github.com/aksakalli/gtop) [gtop](https://github.com/aksakalli/gtop) - A system monitoring dashboard for terminal. Think 'graphical top', with bar charts, line graphs, pie charts, and etc.
- [![Open-Source Software][oss icon]](https://github.com/hishamhm/htop) [htop](http://hisham.hm/htop/) - An interactive process viewer for Unix systems with improved features and user experience
- [![Open-Source Software][oss icon]](https://github.com/nojhan/liquidprompt) [Liquidprompt](https://github.com/nojhan/liquidprompt) - A full-featured & carefully designed adaptive prompt for Bash & Zsh.
- [![Open-Source Software][oss icon]](https://github.com/mps-youtube/mps-youtube) [mps-youtube](https://github.com/mps-youtube/mps-youtube) - A terminal based program for searching, streaming and downloading music. This implementation uses YouTube as a source of content and can play and download video as well as audio.
- [![Open-Source Software][oss icon]](https://gitlab.com/muttmua/mutt) [Mutt](http://www.mutt.org/) - A terminal based mail client with vim keybindings and great flexibility and customizability.
- [![Open-Source Software][oss icon]](https://github.com/dylanaraps/neofetch) [Neofetch](https://github.com/dylanaraps/neofetch/releases) - A fast, highly customizable system info script that supports Linux, MacOS, iOS, BSD, Solaris, Android, Haiku, GNU Hurd, MINIX, AIX and Windows.
- [![Open-Source Software][oss icon]](https://github.com/facebook/PathPicker) [PathPicker](https://github.com/facebook/PathPicker) - A command that lets you select files that were output from a previous command in the command line, so you can then run another command or edit them.
- [![Open-Source Software][oss icon]](https://github.com/dylanaraps/pywal) [pywal](https://github.com/dylanaraps/pywal) - pywal is a script that takes an image (or a directory of images), generates a colorscheme (using imagemagick) and then changes all of your open terminal's colors to the new colorscheme on the fly, allowing you to have your terminal colors change with your wallpaper, or other criteria.
- [![Open-Source Software][oss icon]](https://github.com/orakaro/rainbowstream) [Rainbow Stream](https://github.com/orakaro/rainbowstream) - A smart and nice Twitter client on terminal written in Python.
- [![Open-Source Software][oss icon]](https://github.com/amanusk/s-tui) [s-tui](https://amanusk.github.io/s-tui/) - s-tui is an UI for monitoring your computer's CPU temperature, frequency and utilization in a graphical way from the terminal.
- [![Open-Source Software][oss icon]](https://github.com/nvbn/thefuck) [TheFuck](https://github.com/nvbn/thefuck) - Magnificent app which corrects your previous console command.
- [![Open-Source Software][oss icon]](https://github.com/ggreer/the_silver_searcher) [The Silver Searcher / Ag](https://github.com/ggreer/the_silver_searcher) - A code-searching tool similar to ack, but faster.
- [![Open-Source Software][oss icon]](https://github.com/tmux/tmux) [Tmux](https://tmux.github.io/) - It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. And do a lot more.
- [Top 10 command line tools](http://lifehacker.com/399468/top-10-command-line-tools)
- [![Open-Source Software][oss icon]](https://github.com/soimort/translate-shell) [translate-shell](https://www.soimort.org/translate-shell) - Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
- [![Open-Source Software][oss icon]](https://github.com/jml/undistract-me) [undistract-me](https://github.com/jml/undistract-me) - A command line program that plays a sound or sends a notification when a long command has finished running in the command line.
- [wicd-curses](https://wiki.archlinux.org/index.php/wicd#Running_Wicd_in_Text_Mode) - Command line WiFi connection manager.
- [![Open-Source Software][oss icon]](https://github.com/rg3/youtube-dl) [youtube-dl](http://rg3.github.io/youtube-dl/) - youtube-dl is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter (2.6, 2.7, or 3.2+), and it is not platform specific.

## Desktop Environments

- [![Open-Source Software][oss icon]](https://github.com/solus-project/budgie-desktop) [Budgie](http://www.omgubuntu.co.uk/2016/09/install-budgie-desktop-on-ubuntu) - Budgie is a desktop environment designed with the modern user in mind, it focuses on simplicity and elegance.
- [![Open-Source Software][oss icon]](https://github.com/linuxmint/Cinnamon) [Cinnamon](http://cinnamon.linuxmint.com/) - Cinnamon strives to provide a traditional user experience. Cinnamon is a fork of GNOME 3.
- [![Open-Source Software][oss icon]](https://github.com/linuxdeepin/dde-desktop) [Deepin DE](https://www.deepin.org/en/dde/) - DDE (Deepin Desktop Environment) is the default desktop environment originally created for the Linux Deepin distribution.
- [![Open-Source Software][oss icon]](https://git.enlightenment.org/enlightenment/efl) [Enlightenment](https://www.enlightenment.org/about) - A lightweight and pretty desktop environment that is designed to run fast and look good, while retaining a large degree of customization.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gnome-flashback) [GNOME Flashback](https://wiki.gnome.org/Projects/GnomeFlashback) - GNOME Flashback is a shell for GNOME 3 which was initially called GNOME fallback mode. The desktop layout and the underlying technology is similar to GNOME 2.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gnome-desktop) [Gnome](https://www.gnome.org/) - The GNOME desktop environment is an attractive and intuitive desktop with both a modern (GNOME) and a classic (GNOME Classic) session.
- [![Open-Source Software][oss icon]](https://github.com/KDE/plasma-desktop) [KDE Plasma](https://www.kde.org/workspaces/plasmadesktop/) - The KDE Plasma desktop environment is a familiar working environment. Plasma Desktop offers all the tools required for a modern desktop computing experience so you can be productive right from the start.
- [![Open-Source Software][oss icon]](https://github.com/lxde) [LXDE](http://lxde.org/) - The Lightweight X11 Desktop Environment is a fast and energy-saving desktop environment.
- [![Open-Source Software][oss icon]](https://github.com/lxde/lxqt) [LXQt](http://lxqt.org/) - LXQt is the Qt port and the upcoming version of LXDE, the Lightweight Desktop Environment.
- [![Open-Source Software][oss icon]](https://github.com/mate-desktop/) [Mate](http://mate-desktop.com/) - Mate provides an intuitive and attractive desktop to Linux users using traditional metaphors. MATE is a fork of GNOME 2.
- [![Open-Source Software][oss icon]](https://elementary.io/) [Pantheon](https://elementary.io/) - Pantheon is the default desktop environment originally created for the elementary OS distribution.
- [![Open-Source Software][oss icon]](https://github.com/ubports/unity8) [Unity](https://unity8.io/) - Unity is a shell for GNOME designed by Canonical for Ubuntu. A [guide](http://www.omgubuntu.co.uk/2016/04/ubuntu-16-04-unity-8-desktop-progress-video) on how to install unity 8 on Ubuntu 16.04.
- [![Open-Source Software][oss icon]](https://unity.ubuntu.com) [Unity](https://unity.ubuntu.com/) - Unity is a shell for GNOME designed by Canonical for Ubuntu.
- [![Open-Source Software][oss icon]](https://github.com/xfce-mirror) [Xfce](https://www.xfce.org/) - Xfce embodies the traditional UNIX philosophy of modularity and re-usability.

## Display manager

### Console

- [![Open-Source Software][oss icon]](https://github.com/ghost1227/cdm) [CDM](https://github.com/ghost1227/cdm) - A ultra-minimalistic, yet full-featured login manager written in Bash.
- [![Open-Source Software][oss icon]](https://github.com/dopsi/console-tdm) [Console TDM](https://github.com/dopsi/console-tdm) - An extension for xinit written in pure Bash.
- [![Open-Source Software][oss icon]](https://github.com/spanezz/nodm) [nodm](https://github.com/spanezz/nodm) - A minimalistic display manager for automatic logins.

### Graphic

- [![Open-Source Software][oss icon]](https://github.com/tomas/entrance) [Entrance](http://enlightenment.org) - An EFL based display manager, highly experimental.
- [![Open-Source Software][oss icon]](https://github.com/GNOME/gdm) [GDM](https://wiki.gnome.org/Projects/GDM) - The GNOME display manager.
- [![Open-Source Software][oss icon]](https://github.com/davvid/lightdm) [LightDM](https://www.freedesktop.org/wiki/Software/LightDM) - A cross-desktop display manager, can use various front-ends written in any toolkit.
- [![Open-Source Software][oss icon]](https://sourceforge.net/projects/lxdm/) [LXDM](https://sourceforge.net/projects/lxdm/) - The LXDE display manager. Can be used independent of the LXDE desktop environment.
- [![Open-Source Software][oss icon]](https://github.com/linuxmint/mdm) [MDM](https://github.com/linuxmint/mdm) - The MDM display manager, used in Linux Mint, a fork of GDM 2.
- [![Open-Source Software][oss icon]](https://github.com/sddm/sddm) [SDDM](https://github.com/sddm/sddm) - The QML-based display manager and successor to KDE4's kdm; recommended for Plasma 5 and LXQt.
- [![Open-Source Software][oss icon]](https://github.com/gsingh93/slim-display-manager) [SLiM](https://sourceforge.net/projects/slim.berlios/) - Lightweight and elegant graphical login solution. (discontinued)
- [![Open-Source Software][oss icon]](https://github.com/bbidulock/xdm) [XDM](https://www.x.org/archive/X11R7.5/doc/man/man1/xdm.1.html) - The X display manager with support for XDMCP, and host chooser.

## Window Managers

### Compositors

- [![Open-Source Software][oss icon]](https://github.com/yshui/picom) [Picom](https://github.com/yshui/picom) - Picom is a standalone composite manager, suitable for use with window managers that do not natively provide compositing functionality.
- [![Open-Source Software][oss icon]](https://cgit.freedesktop.org/xorg/app/xcompmgr) [Xcompmgr](https://cgit.freedesktop.org/xorg/app/xcompmgr) - Xcompmgr is a simple composite manager capable of rendering drop shadows and, with the use of the transset utility, primitive window transparency.

### Stacking window managers

- [![Open-Source Software][oss icon]](https://github.com/venam/2bwm) [2bwm](https://github.com/venam/2bwm) - A fast floating WM, with the particularity of having 2 borders, written over the XCB library and derived from mcwm.
- [![Open-Source Software][oss icon]](https://github.com/bbidulock/blackboxwm) [Blackbox](http://blackboxwm.sourceforge.net) - A fast, lightweight window manager for the X Window System, without all those annoying library dependencies.
- [![Open-Source Software][oss icon]](https://github.com/fluxbox/fluxbox) [Fluxbox](http://fluxbox.org) - A window manager for X that was based on the Blackbox 0.61.1 code.
- [![Open-Source Software][oss icon]](https://github.com/danakj/openbox) [Openbox](http://openbox.org) - A highly configurable, next generation window manager with extensive standards support.

### Tiling window managers

- [![Open-Source Software][oss icon]](https://github.com/baskerville/bspwm) [Bspwm](https://github.com/baskerville/bspwm/wiki) - bspwm is a tiling window manager that represents windows as the leaves of a full binary tree.
- [![Open-Source Software][oss icon]](https://github.com/herbstluftwm/herbstluftwm) [Herbstluftwm](https://herbstluftwm.org) - Is a Manual tiling window manager for X11 using Xlib and Glib.
- [![Open-Source Software][oss icon]](https://github.com/i3/i3) [i3 WM](https://i3wm.org/) - A better tiling and dynamic window manager. It's completely written from scratch. The target platforms are GNU/Linux and BSD operating systems.
- [![Open-Source Software][oss icon]](https://github.com/qtile/qtile) [Qtile](https://www.qtile.org/) - qtile is a full-featured, hackable tiling window manager written and configured in Python.
- [![Open-Source Software][oss icon]](https://github.com/swaywm/sway) [Sway](http://swaywm.org) - Sway is tiling Wayland compositor and a drop-in replacement for the i3 window manager for X11.

### Dynamic window managers

- [![Open-Source Software][oss icon]](https://github.com/awesomeWM/awesome) [awesome](https://awesomewm.org) - A highly configurable, next generation framework window manager for X.
- [![Open-Source Software][oss icon]](https://github.com/cdown/dwm) [dwm](http://dwm.suckless.org) - A dynamic window manager for X. It manages windows in tiled, monocle and floating layouts.
- [![Open-Source Software][oss icon]](https://github.com/i3/i3) [i3](https://i3wm.org) - Tiling window manager, completely written from scratch.
- [![Open-Source Software][oss icon]](https://github.com/conformal/spectrwm) [spectrwm](https://github.com/conformal/spectrwm/wiki) - A small dynamic tiling window manager for X11, largely inspired by xmonad and dwm.
- [![Open-Source Software][oss icon]](https://github.com/xmonad/xmonad) [xmonad](http://xmonad.org) - A dynamically tiling X11 window manager that is written and configured in Haskell.

## Setup

- [What is Linux](https://www.linux.com/what-is-linux)
- [Basic Linux terms](http://www.makeuseof.com/tag/linux-confusing-key-terms-definitions/)
- [Choosing Distro that Suits You Best](http://i.imgur.com/TV21DgN.jpg)
- [38 Things To Do After Installing Ubuntu](https://www.lifewire.com/things-to-do-installing-ubuntu-2200611)
- [What do the commands on the command line mean?](https://www.explainshell.com) [![Open-Source Software][oss icon]](https://github.com/idank/explainshell)

### Arch Linux

- [Getting and installing Arch](https://wiki.archlinux.org/title/installation_guide)
- [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)
- [General recommendations](https://wiki.archlinux.org/index.php/General_recommendations)
- [List of applications](https://wiki.archlinux.org/index.php/List_of_applications)

### Bodhi

- [What is Bodhi](https://en.wikipedia.org/wiki/Bodhi_Linux)
- [Where to download Bodhi](http://www.bodhilinux.com/download/)
- [How do I install Bodhi](http://www.bodhilinux.com/w/installation-instructions/)

### CentOS

- [Official website](https://www.centos.org)
- [About](https://wiki.centos.org/About)
- [Downloads](https://wiki.centos.org/Download)
- [Manuals](https://www.centos.org/docs/)
- [Tips and Tricks](https://wiki.centos.org/TipsAndTricks)
- [FAQ](https://www.centos.org/forums/faq.php?sid=4e6d260284c7936505dcf75564717272)

### Fedora

- [What is Fedora?](https://docs.fedoraproject.org/fedora-project/project/fedora-overview.html)
- [Where to download Fedora](https://getfedora.org)
- [How do I install Fedora?](https://docs.fedoraproject.org/f26/install-guide/install/Preparing_for_Installation.html)
- [Ask Fedora](https://ask.fedoraproject.org/c/english/97)

### openSUSE

- [What is openSUSE](https://www.techopedia.com/definition/28543/opensuse)
- [Reasons to try openSUSE](http://www.pcworld.com/article/222065/5_reasons_to_try_opensuse_114.html)
- [Beginner's FAQ](https://en.opensuse.org/openSUSE:OpenSUSE_for_beginners)
- [How to install openSUSE](https://en.opensuse.org/Portal:Installation)
- [Review](https://www.linux.com/news/opensuse-leap-421-review-most-mature-linux-distribution)

### Ubuntu

- [What is Ubuntu](<https://en.wikipedia.org/wiki/Ubuntu_(operating_system)>)
- [How to install Ubuntu](http://www.ubuntu.com/download/desktop/install-ubuntu-desktop)
- [How to dual-boot Ubuntu with Windows](http://www.everydaylinuxuser.com/2014/05/install-ubuntu-1404-alongside-windows.html)
- [What to do after installing Ubuntu](http://www.omgubuntu.co.uk/2016/04/10-things-to-do-after-installing-ubuntu-16-04-lts)

### Other distros

> To be added later

## Discussion Forums

### Arch Linux Forums

- [Arch Linux Forums](https://bbs.archlinux.org/)
- [Arch Linux ARM Forums](https://archlinuxarm.org/forum/viewforum.php?f=31)

### Bodhi Linux Forums

- [Bodhi Linux Forums](http://forums.bodhilinux.com/)

### CentOS Forums

- [CentOS Forums](https://www.centos.org/forums/)

### Fedora Forums

- [Fedora Forums](https://forums.fedoraforum.org/index.php)

### Ubuntu Forums

- [Ubuntu Forum](https://ubuntuforums.org/)
- [Ask Ubuntu](askubuntu.com/)

### openSUSE Forums

- [openSUSE Forum](https://forums.opensuse.org/forum.php)

### IRC channels

- [#linux](http://webchat.freenode.net/?channels=#linux)
- [#ubuntu](https://webchat.freenode.net/?channels=ubuntu)
- [#archlinux](http://webchat.freenode.net/?channels=archlinux)
- [#debian](http://webchat.freenode.net/?channels=debian)
- [#gentoo](http://webchat.freenode.net/?channels=gentoo)
- [#docker](http://webchat.freenode.net/?channels=docker)
- [#bash](http://webchat.freenode.net/?channels=bash)

### Linux News, Apps, and more:

- [OMG!Ubuntu](http://www.omgubuntu.co.uk/)
- [ITSFOSS](https://itsfoss.com/)
- [Linux official](https://www.linux.com/)
- [Webupd8](http://www.webupd8.org/)
- [Noobslab](http://www.noobslab.com/)
- [Make use of](http://www.makeuseof.com/service/linux/)
- [TecMint](http://www.tecmint.com/)
- [AllTop](http://linux.alltop.com/)
- [Unixmen](https://www.unixmen.com/)
- [DistroWatch](http://distrowatch.com/)
- [Phoronix](http://www.phoronix.com/)
- [Dedoimedo](http://www.dedoimedo.com/)
- [How-To Geek](http://www.howtogeek.com/t/linux/)
- [Liliputing](http://liliputing.com/)
- [FAMILUG](http://www.familug.org/)
- [Ubuntu Geek](http://www.ubuntugeek.com/)

### Reddit

- [Arch Linux](https://www.reddit.com/r/archlinux/)
- [CentOS](https://www.reddit.com/r/CentOS/)
- [Fedora](https://www.reddit.com/r/Fedora/)
- [Linux](https://www.reddit.com/r/linux/)
- [Open Source](https://www.reddit.com/r/opensource/)
- [Ubuntu](https://www.reddit.com/r/Ubuntu/)
- [Unix Porn](https://www.reddit.com/r/unixporn/)
- [Linux Kernel](https://www.reddit.com/r/kernel/)
- [Linux Gaming](https://www.reddit.com/r/linux_gaming/)

## Learn Linux

- [Beginner's guide to Linux](https://www.linux.com/learn/complete-beginners-guide-linux%20)
- [Learn Linux Command](http://linuxcommand.org/)
- [GNU/Linux Command-Line Tools Summary](http://tldp.org/LDP/GNU-Linux-Tools-Summary/html/book1.htm)
- [Learn Linux](https://linuxjourney.com/)
- [Linux Course](https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0)
- [Linux Pocket Guide](http://www.tldp.org/LDP/Pocket-Linux-Guide/Pocket-Linux-Guide.pdf)

## Linux Hacking/Development

- [Kernel Newbies](https://kernelnewbies.org/)
- [Linux Insides](https://0xax.gitbooks.io/linux-insides/content/index.html)
- [The Linux Kernel](http://www.tldp.org/LDP/tlk/tlk.html)
- [Linux Kernel Archives (Official Website)](https://www.kernel.org/)
- [Linux Kernel Internals (PDF)](http://www.tldp.org/LDP/lki/lki.pdf)
- [Linux Kernel Mailing List Archive](https://lkml.org/)
- [Linux Kernel Module Programming Guide (PDF)](http://www.tldp.org/LDP/lkmpg/2.6/lkmpg.pdf)

## Advanced Linux

- [Virtual Containers](https://github.com/Citrix-TechSpecialist/Docker-101)
- [Virtualization with Virtualbox](https://www.virtualbox.org/manual/ch01.html)

## Other Awesome Lists

_These are the list that I highly recommended:_

- [Awesome Linux Audio](https://github.com/nodiscc/awesome-linuxaudio)
- [Awesome Self-hosted](https://github.com/kickball/awesome-selfhosted)
- [Awesome Sysadmin](https://github.com/n1trux/awesome-sysadmin)

## Contributors

Thanks to [**All of Github contributors**](https://github.com/LewisVo/Awesome-Linux-Software/graphs/contributors) for making this list possible and
_Everyone @ reddit.com/r/linux & reddit.com/r/ubuntu & vozforums.com & other forums for many suggestions and compliments_
...

**[⬆ back to top](#table-of-contents)**

<br>

## Guidelines to contribute

> Simply put the name of the **application** in the list.
> Link to its **homepage** or a **guide** on how to install it.
> Also write a **short description** for the application + add **icon**.
> Make sure it is put under the **appropriate topic**.
> If the application doesn't fit in any **existing topic**, make a **new one** for it.
> Ensure everything is **alphabetically sorted**.

## Unsure how to contribute?

- [How to Use Github](https://guides.github.com/activities/forking/)
- [How to Git from the Command Line](https://rogerdudler.github.io/git-guide/)
- [What is Markdown?](https://github.com/LewisVo/Markdown-Tutorial) - Markdown is the writing method used to create this list, if you want to know how to format properly, it's best that you learn how to use Github Markdown.
- [Alternative Markdown Guide:](https://guides.github.com/features/mastering-markdown/)

_Items marked with ![Open-Source Software][oss icon] are open-source software and link to the source code. Items marked with [![Nonfree][money icon] are nonfree (as in nonfree beer) and may cost money to use._

<br>

_Author's note: Recently, I received feedbacks from you about the quality of some applications on this list. I myself tested them out a lot (not all of them, though). If you have any problems with the apps, please: -> head to the dev page (if available) -> make an issue for the dev there -> make an issue here so that I can consider whether I should get the app out of the list. Remember : Everything has its own quality, so there will never be anything like "best app" or "selective list" here, thank you._

<br>

## License

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[oss icon]: https://cdn.rawgit.com/iCHAIT/awesome-osx/master/media/oss.svg
[money icon]: https://rawgit.com/LewisVo/Awesome-Linux-Software/master/img/money.svg

<!-- markdown-link-check-enable -->
