#include <cmath> 
#include <cstring>
#include <initializer_list>

template<typename T>
struct vector3 
{
    typedef const vector3 & ref;
public:
    union
    {
        struct {T x, y, z;};
        struct {T r, g, b;};
        T data[3];
    };
       
    vector3(const T _x = 0, const T _y = 0 ,const T _z = 0) : 
        x(_x), y(_y),z(_z)
    {}
    vector3(std::initializer_list<T> l) 
    {
        std::memcpy(data,l.begin(),sizeof(data));
    }   

    vector3   operator-  () const {return vector3(-x,-y,-z);}
    T  operator*  (const vector3 &a)  const {return x * a.x + y * a.y + z * a.z;}
    vector3   operator*  (const T a)  const {return vector3( x * a, y * a, z * a);}
    vector3   operator+  (const vector3 &a)  const {return vector3(x + a.x, y + a.y, z+ a.z);}
    vector3   operator-  (const vector3 &a)  const {return vector3(x - a.x, y - a.y, z- a.z);}
    vector3 & operator+= (const vector3 &a)  {x += a.x; y += a.y; z += a.z; return *this;}
    vector3 & operator-= (const vector3 &a)  {x -= a.x; y -= a.y; z -= a.z; return *this;}
    vector3 & operator/= (const vector3 &a)  {x /= a.x; y /= a.y; z /= a.z; return *this;}
    vector3 & operator*= (const T a) {x *= a; y *= a; z *= a; return *this; }
  
    bool   operator== (const vector3 &a)  const {return compare(a);}
    bool   operator!= (const vector3 &a)  const {return !compare(a);}
    
    bool  compare(const vector3 &a) const {return ((x == a.x) && (y == a.y) && (z == a.z));}
    T length()  const {return std::sqrt(x * x + y * y + z * z);}
    vector3  cross(const vector3 &a) const
    {
        return vector3({y * a.z - z * a.y, z * a.x - x * a.z, x * a.y - y * a.x});
    }

    
    friend vector3 operator* (const T a, const vector3 b) {return vector3( b.x * a, b.y * a, b.z * a);}
};
using vec3 = vector3<float>;
