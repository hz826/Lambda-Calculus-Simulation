### basic

```
f = \x -> x
```

### high order function & currying
```
g = \x -> \y -> x y
```

### bool logic

```
true  = \x -> \y -> x
false = \x -> \y -> y
if    = \b -> \t -> \f -> b t f
not   = \b -> \x -> \y -> b y x
and   = \x -> \y -> if x y false
or    = \x -> \y -> if x true y
```

### church number

```
zero  = \f -> \x -> x
one   = \f -> \x -> f x
two   = \f -> \x -> f(f x)
three = \f -> \x -> f(f (f x))
succ  = \n -> \f -> \x -> f(n f x)
add   = \a -> \b -> a succ b
mult  = \a -> \b -> a (add b) zero
pred  = \n -> \f -> \x -> n (\g -> \h -> h(g f)) (\u -> x) (\u -> u)
minus = \a -> \b -> b pred a
```

### TEST

```
f     = \x -> x
g     = \x -> \y -> x y
true  = \x -> \y -> x
false = \x -> \y -> y
if    = \b -> \t -> \f -> b t f
not   = \b -> \x -> \y -> b y x
and   = \x -> \y -> if x y false
or    = \x -> \y -> if x true y

zero  = \f -> \x -> x
one   = \f -> \x -> f x
two   = \f -> \x -> f(f x)
three = \f -> \x -> f(f(f x))
succ  = \n -> \f -> \x -> f(n f x)
four  = succ three
five  = succ four
six   = succ five
seven = succ six
eight = succ seven
nine  = succ eight
ten   = succ nine

add   = \a -> \b -> a succ b
mult  = \a -> \b -> a (add b) zero
pred  = \n -> \f -> \x -> n (\g -> \h -> h(g f)) (\u -> x) (\u -> u)
minus = \a -> \b -> b pred a

and true false
and true true
or true false
or false false
add two three
add one
mult three three
minus nine four
```