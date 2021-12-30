#<!--(c) Code-X-Mania-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta property="og:image" content="https://www.flaticon.com/premium-icon/icons/svg/2626/2626281.svg" itemprop="thumbnailUrl">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%s</title>
    <link rel="stylesheet" type='text/css' href="https://drive.google.com/uc?export=view&id=1pVLG4gZy7jdow3sO-wFS06aP_A9QX0O6">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Delius">
    <link rel="stylesheet" href="https://cdn.plyr.io/3.5.6/plyr.css" />
    <!-- <link rel="stylesheet" href="style.css"> -->

</head>

<body>
    <header>
        <div class="toogle"></div>
        <div id="file-name">
            %s
        </div>
    </header>

    <div class="container">
        <tag src="%s" class="player"></tag>
    </div>
    
    <footer>
        <span id="fork-text">Join My Telegram Channel</span>
        <span>
            <a href="https://t.me/tellybots_4u" id='github-logo'>
                <svg id='octo' style="width: 1.2rem; padding-left: 5px; fill: var(--footer-icon-color)" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
        </span>
    </footer>
    
    
    <script src="https://cdn.plyr.io/3.5.6/plyr.js"></script>
	<script>
        const controls = [
              'play-large',
              'rewind',
              'play', 
              'fast-forward', 
              'progress', 
              'current-time',
              'duration',
              'mute',
              'volume',
              'captions',
              'settings',
              'pip',
              'airplay',
              'download',
              'fullscreen'
            ];
        document.addEventListener('DOMContentLoaded', () => {
            const player = Plyr.setup('.player', { controls });
        });

        const body = document.querySelector('body');
        const footer = document.querySelector('footer');
        const toogle = document.querySelector('.toogle');
        toogle.onclick = () => {
            body.classList.toggle('dark')
            footer.classList.toggle('dark')
        }
    </script>
</body>
</html>
