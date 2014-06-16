Shader "iFree/simplest" 
{	
	SubShader 
	{
	  Pass 
	  { 
	  	GLSLPROGRAM 
	  	#ifdef VERTEX
	     void main() 
         {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
         }
 
      #endif
      #ifdef FRAGMENT 
         void main() 
         {
            gl_FragColor = vec4(1.0,0.0,0.0,1.0);
         }
 
      #endif 
      ENDGLSL 
      }
   }
}