Shader "iFree/template" 
{
	Properties 
	{
		_MainTex ("Base (RGB)", 2D) = "white" {}
	}
	SubShader 
	{
	  Pass 
	  { 
	  	GLSLPROGRAM 
	  	#ifdef VERTEX
	  	#include "UnityCG.glslinc"
         varying vec2 textureCoordinates;
         void main() 
         {
            textureCoordinates = gl_MultiTexCoord0.xy;
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
         }
 
      #endif
      #ifdef FRAGMENT 
         uniform sampler2D _MainTex;   
         varying vec2 textureCoordinates;
         void main() 
         {
            gl_FragColor = texture2D(_MainTex, textureCoordinates);
         }
 
      #endif 
      ENDGLSL 
      }
   }
}