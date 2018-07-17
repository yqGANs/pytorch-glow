import torch


def reduce_mean(tensor, dim=None, keepdim=False, out=None):
    """
    Returns the mean value of each row of the input tensor in the given dimension dim.

    Support multi-dim mean

    :param tensor: the input tensor
    :type tensor: torch.Tensor
    :param dim: the dimension to reduce
    :type dim: int or list[int]
    :param keepdim: whether the output tensor has dim retained or not
    :type keepdim: bool
    :param out: the output tensor
    :type out: torch.Tensor
    :return: mean result
    :rtype: torch.Tensor
    """
    # mean all dims
    if dim is None:
        return torch.mean(tensor)
    # prepare dim
    if isinstance(dim, int):
        dim = [dim]
    dim = sorted(dim)
    # get mean dim by dim
    for d in dim:
        tensor = tensor.mean(dim=d, keepdim=True)
    # squeeze reduced dimensions if not keeping dim
    if not keepdim:
        for cnt, d in enumerate(dim):
            tensor.squeeze_(d - cnt)
    if out is not None:
        out.copy_(tensor)
    return tensor


def reduce_sum(tensor, dim=None, keepdim=False, out=None):
    """
    Returns the sum of all elements in the input tensor.

    Support multi-dim sum

    :param tensor: the input tensor
    :type tensor: torch.Tensor
    :param dim: the dimension to reduce
    :type dim: int or list[int]
    :param keepdim: whether the output tensor has dim retained or not
    :type keepdim: bool
    :param out: the output tensor
    :type out: torch.Tensor
    :return: sum result
    :rtype: torch.Tensor
    """
    # summarize all dims
    if dim is None:
        return torch.sum(tensor)
    # prepare dim
    if isinstance(dim, int):
        dim = [dim]
    dim = sorted(dim)
    # get summary dim by dim
    for d in dim:
        tensor = tensor.sum(dim=d, keepdim=True)
    # squeeze reduced dimensions if not keeping dim
    if not keepdim:
        for cnt, d in enumerate(dim):
            tensor.squeeze_(d - cnt)
    if out is not None:
        out.copy_(tensor)
    return tensor


def tensor_equal(a, b, eps=1e-6):
    """
    Compare two tensors

    :param a: input tensor a
    :type a: torch.Tensor
    :param b: input tensor b
    :type b: torch.Tensor
    :param eps: epsilon
    :type eps: float
    :return: whether two tensors are equal
    :rtype: bool
    """
    if a.shape != b.shape:
        return False

    return 0 <= float(torch.max(torch.abs(a - b))) <= eps