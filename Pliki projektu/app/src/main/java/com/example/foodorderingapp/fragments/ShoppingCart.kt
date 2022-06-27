package com.example.foodorderingapp.fragments

import android.os.Bundle
import android.util.Log
import android.view.*
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.foodorderingapp.R
import com.example.foodorderingapp.databinding.FragmentShoppingCartBinding
import com.example.foodorderingapp.model.Order
import com.example.foodorderingapp.model.ShoppingCard
import com.example.foodorderingapp.viewmodel.OrderViewModel

class ShoppingCart : Fragment() {

    private var _binding: FragmentShoppingCartBinding? = null
    private val binding get() = _binding!!
    private lateinit var viewModel: OrderViewModel

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        setHasOptionsMenu(true)
        viewModel = ViewModelProvider(this)[OrderViewModel::class.java]
        _binding = FragmentShoppingCartBinding.inflate(inflater, container, false)
        val cartView = binding.cartRecyclerView
        cartView.layoutManager = LinearLayoutManager(requireContext())
        val adapter = ShoppingCartAdapter()
        cartView.adapter = adapter

        Log.i("KOSZYK", ShoppingCard.shoppingList.toString())
        adapter.setData(ShoppingCard.shoppingList)

        binding.sumTxt.text = String.format("%.2f", ShoppingCard.getFinalPrice()) + " zł"
        val order = Order(
            "delivery",
            restaurant = ShoppingCard.getRestaurant()!!.code,
            shoppingList = ShoppingCard.shoppingList
            )

        binding.clearCartBtn.setOnClickListener{
            clearCart(adapter)
        }

        binding.orderBtn.setOnClickListener{
            viewModel.addOrder(order)
            Toast.makeText(it.context, "Zamówienie złożone", Toast.LENGTH_SHORT).show()
            clearCart(adapter)
            view?.findNavController()?.popBackStack(R.id.homePage, false)
        }

        return binding.root
    }
    override fun onCreateOptionsMenu(menu: Menu, inflater: MenuInflater) {
        inflater.inflate(R.menu.menu_back, menu)
        super.onCreateOptionsMenu(menu, inflater);
    }
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.back_button -> {
                view?.findNavController()?.popBackStack()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
    fun clearCart(adapter: ShoppingCartAdapter){
        ShoppingCard.clearCard()
        adapter.setData(ShoppingCard.shoppingList)
        binding.sumTxt.text = String.format("%.2f", ShoppingCard.getFinalPrice()) + " zł"
    }
}