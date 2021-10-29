using Plots
using ImageView

# check out https://github.com/chakravala/Fatou.jl

function meshgrid(x, y)
    X = [x for _ in y, x in x]
    Y = [y for y in y, _ in x]
    X, Y
 end

function juliaset(precision=1000,n_iter=200)
    # Grid space
    x = range(-2,2,length=precision)
    y = range(-2,2,length=precision)

    xx,yy = meshgrid(x,y)

    c = vec(xx) + vec(yy).*1im
    z = zeros(precision.^2)

    n_iter_diverg = zeros(size(z))
    not_div = ones(Bool,size(z))

    for i in 1:n_iter
        z = z.^2 + c
        not_div = abs.(z) .< 2 
        n_iter_diverg[not_div] = n_iter_diverg[not_div] .+ 1
    end

    ImageView.imshow(reshape(log.(n_iter_diverg),(precision,precision)))
    
end 

juliaset()