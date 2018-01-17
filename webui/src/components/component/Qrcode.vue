<template>
    <div class="uk-flex uk-flex-column uk-form ">
        <textarea class='uk-responsive-width uk-responsive-height' data-uk-grid-match="{target:'#generate'}" id='text' placeholder="Text here"></textarea>
        <div>
            <div class="uk-flex uk-margin-top uk-margin-bottom uk-flex-space-around">
                <button class='uk-button' @click.prevent="generate()">Generate</button>
                <button class='uk-button' @click.prevent="clr()">Clear</button>
            </div>
        </div>
        <div class='uk-panel uk-align-center'>
            <div id="output"></div>
        </div>
    </div>
</template>

<script>
    import QRCode from 'jquery.qrcode'

    export default {
        methods: {
            clr: function () {
                $('#output').text('');
            },
            toUtf8: function (str) {
                var out, i, len, c;
                out = "";
                len = str.length;
                for (i = 0; i < len; i++) {
                    c = str.charCodeAt(i);
                    if ((c >= 0x0001) && (c <= 0x007F)) {
                        out += str.charAt(i);
                    } else if (c > 0x07FF) {
                        out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
                        out += String.fromCharCode(0x80 | ((c >> 6) & 0x3F));
                        out += String.fromCharCode(0x80 | ((c >> 0) & 0x3F));
                    } else {
                        out += String.fromCharCode(0xC0 | ((c >> 6) & 0x1F));
                        out += String.fromCharCode(0x80 | ((c >> 0) & 0x3F));
                    }
                }
                return out;
            },
            generate: function () {
                this.clr();
                $('#output').qrcode(this.toUtf8($('#text').val()));
            }
        }
    }
</script>
