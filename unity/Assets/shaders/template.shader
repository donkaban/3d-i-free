Shader "Custom/simple" 
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
         void main() 
         {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
         }
 
      #endif
      #ifdef FRAGMENT 
         
         void main() 
         {
            gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0); 
         }
 
      #endif 
      ENDGLSL 
      }
   }
}