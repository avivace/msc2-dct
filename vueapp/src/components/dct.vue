<template>
	<div class="hello">
		  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
    	<v-flex xs12>
		<center><h1 style="font-size:64px; font-weight: 300">MCS2 - DCT2 UI </h1></center>
		<span style="font-size:18px;font-weight: 400"> Antonio Vivace,  February 2019</span>
		
		<form enctype="multipart/form-data">
		<input type="file" name="sourceImage" @change="filesChange($event.target.files);"
						accept="image/*" class="input-file">
				</form>
    	</v-flex>
      <v-flex xs6 v-if="startingImage">
      	<center>
      	<div v-bind:style="{ maxWidth: width + 'px' }">
      	<span style="font-size:24px">Source</span><br>
        		<img width="100%"  :src=startingImage >
        	</div>
        </center>
      </v-flex>
      	
            <v-flex xs6 v-if="startingImage">

            <span style="font-size:24px">Processed</span><br>
            <center>
      	<div v-bind:style="{ maxWidth: width + 'px' }">

        		<img width="100%" :src=outputImage >
</div>
</center>
      </v-flex>
      <v-flex xs6 v-if="startingImage">
      	    <v-btn flat large outline
      :loading="loading"
      :disabled="loading"
      
      @click="update"
    >
      Applica
    </v-btn>
<br>
		<div class="slidecontainer">
			<template v-if="imageReady">
  <b>d</b>= &nbsp;<input width=100 type="range" min="0" :max="height+width-2" v-model="d" class="slider" id="dSlider"> {{ d}} <br>
  <b>b</b>= &nbsp;<input type="number" step="1" v-model="beta"><br><br>
  			<pre>{{ height }} x {{width }}</pre><br>

</template>
</div>
</v-flex>
<v-flex xs6>
	<center>
      <apexchart v-if="outputReady" height="200" width="640" type="bar" :options="chartOptions" :series="series"></apexchart>
  </center>
</v-flex>
    </v-layout>

  </v-container>

	</div>
</template>

<script>
import VueCharts from 'vue-chartjs'
import { Bar, Line } from 'vue-chartjs'

export default {
	data: function(){ return {
		series: [{
          name: 'DCT2',
          data: [0]
        }, {
          name: 'Pre',
          data: [0]
        }, {
          name: 'IDCT2',
          data: [0]
        }, {
          name: 'Norm',
          data: [0]
        }, {
          name: 'Beta',
          data: [0]
        }],
        chartOptions: {
          chart: {
            stacked: true,
            fontFamily: 'Inter, Helvetica, Arial, sans-serif',
            fontSize: '21px'
          },
          plotOptions: {
            bar: {
              horizontal: true,
            },

          },
          stroke: {
            width: 1,
            colors: ['#fff']
          },

          xaxis: {
            //categories: ['time'],
            labels: {
            	fontSize: '21px',
              formatter: function (val) {
                return val + "s"
              }
            }
          },
          yaxis: {
            title: {
              text: undefined
            },

          },
          tooltip: {
            y: {
            	fontSize: '21px',
              formatter: function (val) {
                return val + "s"
              }
            }
          },
          fill: {
            opacity: 1

          },

          legend: {
          	fontSize: '16px',
            position: 'top',
            horizontalAlign: 'left',
            offsetX: 40
          }
        },
      
		startingImage: null,
		height: null,
		width: null,
		outputImage:null,
		d:0,
		imageReady: false,
		imageData: null,
		beta:1,
		loading: false,
		loader: null,
		timings: null,
		outputReady: false,
	}},
	methods:{
		update: function(){
			// Upload it to the backend
			this.loading = true;
			var formData = new FormData();
			formData.append("sourceImage", this.imageData);
			formData.append("d", this.d)
			formData.append("beta", this.beta)
			var self = this;
			this.$axios.post('http://localhost:5000/image', formData, {
				headers: {
					'Content-Type': 'multipart/form-data'
					}
				})  
			.then(function (response) {
				self.outputReady = true;
				self.outputImage = response.data.image
				console.log(self.series[0].data[0])
				self.series	= [{
          name: 'DCT2',
          data: [response.data.dct2Time]
        }, {
          name: 'Pre',
          data: [response.data.preTime]
        }, {
          name: 'IDCT2',
          data: [response.data.idct2Time]
        }, {
          name: 'Norm',
          data: [response.data.normTime]
        }, {
          name: 'Beta',
          data: [response.data.betaTime]
        }]
        				self.timings = {
					'dct2': response.data.dct2Time,
					'pre' : response.data.preTime,
					'idct2Time': response.data.idct2Time,
        			'betaTime': response.data.betaTime,
        			'normTime': response.data.normTime,
        			'totalTime': response.data.totalTime
				}
				self.loading = false;
			})
			.catch(function (error) {
				console.log(error);
			});
		},
		filesChange: function(file){
			var reader = new FileReader();

			// Render the selected image
			reader.onload = function(e){
				this.imageReady = true,
				//console.log(e.target.result)
				this.startingImage = e.target.result;
				let image = new Image();
				image.src = e.target.result;
				//console.log(image)

				// Once it's ready, read height and width
				image.onload = function() {
					this.height = image.height;
					this.width = image.width;
				}.bind(this)

			}.bind(this)

			reader.readAsDataURL(file[0]);

			this.imageData = file[0]
			
		}
	}
}
</script>

<style>
@import url('https://rsms.me/inter/inter.css');
html { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  html { font-family: 'Inter var', sans-serif; }
}
html{
	font-family: 'Inter';
}
.apexcharts-legend-text {
	font-family: 'Inter';
} 

img{
  
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 5px;
  -moz-box-shadow: rgba(0,0,0,0.5) 0 2px 5px;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 5px;
}
.slidecontainer{
	font-size:24px;
}
input[type="number"] {
   width:75px;
}
[class^="apex"], [class*=" apex"] { 
font-size:12px;
 }
</style>
