description = "Short mode description, text, code, circuit, more text. "
var api_url = 'http://localhost:5000/';
var test_mode_api = "api/v1/test_mode/run";

var led_on_api = "api/v1/led_on_mode/run"
var led_on_api_url =api_url+ led_on_api;
var led_off_api = "api/v1/led_off_mode/run"
var led_off_api_url =api_url+ led_off_api;

mode = {
    id:"distance-mesurement",
    title:"Distance Mesurement",
    description:description,
    icon:"assets/icons/Motor.svg",
    api:api_url+test_mode_api  
}
mode2 = {
    id:"liquid-level",
    title:"Liquid Level",
    description:description,
    icon:"assets/icons/Mosfet.svg",
    api:api_url+test_mode_api
}
led_on_mode= {
    id:"blincking-led",
    title:"Blinking LED",
    description:description,
    icon:"assets/icons/LED.svg",
    api:api_url+"api/v1/led_on_mode/run"
}
var modes = [mode, mode2, led_on_mode]

function render_modes(modes){
    modes.forEach(mode => {
        modeUI = `
        <div class="mode-element" id="${mode.id}">
            <div class="mode-element-content">
                <div class="mode-icon rel">
                    <div class="cntr">
                        <img src="${mode.icon}" alt="LED" width="30px">
                    </div>
                </div>
                <div class="mode-details">
                    <div class="mode-title">
                        ${mode.title}
                    </div>
                    <div class="mode-description">
                        ${mode.description}
                    </div>
                </div>
            </div>
        </div>                    `
        $(".browse-content").append(modeUI)
    });
}
render_modes(modes);

$(".blincking-led").click(function (){
    console.log("led switched");
})

function test_mode(){
    // testing the api functionality 
    var api_url = 'http://localhost:5000/'
    api_url+='api/v1/test_mode/run'
    $.get( api_url, function( data ) {
        console.log(data);
    });
}

  $(".mode-element").click(function (){
    var title = $(this).find(".mode-title").text();
    console.log(title);
    test_mode();
  })